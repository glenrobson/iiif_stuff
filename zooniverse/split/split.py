#! /usr/bin/env python3

import json 
from urllib import request
from urllib.parse import urlparse
import os
import base64

def loadJson(url):
    with request.urlopen(url) as data:
        return json.loads(data.read())

def createAnnoPage():
    annoPage = {
        "@context": "http://iiif.io/api/presentation/3/context.json",
        "type": "AnnotationPage",
        "partOf": {
            "id": "https://zooniverse.github.io/iiif-annotations/annotations/titles.json",
            "type": "AnnotationCollection"
        },
        "items": []
    }

    return annoPage

if __name__ == "__main__":
    base = "https://glenrobson.github.io/iiif_stuff/zooniverse/split"

    annotations = loadJson('https://zooniverse.github.io/iiif-annotations/annotations/titles/0.json')

    # split annotations in to one annotation page per canvas
    annoMap = {}
    for anno in annotations['items']:
        canvas = anno['target'].split("#")[0]
        if canvas not in annoMap:
            annoMap[canvas] = createAnnoPage()

        annoMap[canvas]['items'].append(anno)

    # add links to annotation pages to correct canvas
    manifest = loadJson('https://api.bl.uk/metadata/iiif/ark:/81055/vdc_100022589176.0x000002/manifest.json')
    canvasNo = 0
    for canvas in manifest['sequences'][0]['canvases']:
        if canvas['@id'] in annoMap:
            print ('Adding annotations to canvas no: {}'.format(canvasNo))

            # Write out annotation page 
            filename = "annoPage-{}.json".format(canvasNo)
            annoPage = annoMap[canvas['@id']]
            annoPageURL = "{}/{}".format(base, filename)
            annoPage['id'] = annoPageURL
            with open(filename, 'w') as outfile:
                json.dump(annoPage, outfile)

            # Add link to manifest pointing to annotation page
            canvas['annotations'] = [{
                "id": annoPageURL, # add the URL to the annotation page to the manifest
                "type": "AnnotationPage"
            }]

        canvasNo += 1            

    # Write out the manifest with annotation links to file
    with open('manifest.json', 'w') as outfile:
        json.dump(manifest, outfile)
