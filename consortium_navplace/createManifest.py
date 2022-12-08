import csv

from iiif_prezi3 import Manifest, config
import requests
from io import StringIO
import io
import mimetypes
import PIL

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base="https://glenrobson.github.io/iiif_stuff/consortium_navplace"

manifest = Manifest(id=base + "/manifest.json", label="Consoritum Members with navPlace from Wikidata")

with open('members.csv') as csvfile:

    spreadsheet = csv.reader(csvfile)

    img = 0

    for row in spreadsheet:
        if img != 0:
            print(', '.join(row))
            canvas = manifest.make_canvas(id="{}/canvas/{}".format(base, img))
            inst_img = row[3]
            if not inst_img:
                inst_img = row[4]

            canvas.label = row[1]    
            if row[2]:
                pointTxt = row[2].replace('Point(','').replace(')', '')
                latlong = pointTxt.split(' ')
                canvas.navPlace = {
                    "id": "http://example.com/feature-collection/1",
                    "type": "FeatureCollection",
                    "features":[{
                        "id": "http://example.com/feature/1",
                        "type": "Feature",
                        "properties":{},
                        "geometry":{
                            "type": "Point",
                            "coordinates":[
                                latlong[0],
                                latlong[1]
                            ]
                        }
                    }]
                }
                    
                if inst_img:    
                    headers = {'User-Agent': 'GlensProg/0.0 (https://iiif.io; glen.robson@iiif.io)'}    
                    req = requests.get(inst_img, headers=headers)
                    try:
                        canvas.set_hwd_from_file(io.BytesIO(req.content))

                        img_format = ""
                        if inst_img[-3:] == 'png':
                            img_format = "image/png"
                        elif inst_img[-3:] == 'jpg' or inst_img[-3:] == 'JPG':   
                            img_format = "image/jpg"
                        elif inst_img[-3:] == 'svg':   
                            img_format = "image/svg"
                        else:
                            print ('Unknown extension: {} from {}'.format(inst_img[-3:], inst_img))
                            exit(-1)

                        print ('Height: {} width: {} format: {}'.format(canvas.height, canvas.width, img_format))

                        anno_page = canvas.add_image(image_url=inst_img,
                                             anno_page_id="{}/canvas/{}/page".format(base,img),
                                             anno_id="{}/canvas/{}/annotation".format(base,img),
                                             format=img_format,
                                             height=canvas.height,
                                             width=canvas.width
                                             )
                    except PIL.UnidentifiedImageError:
                        print ('Couldnt identify {}'.format(inst_img))

        img += 1

print(manifest.json(indent=2))        
