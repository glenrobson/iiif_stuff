#! /usr/bin/env python3

import json 
import os

if __name__ == "__main__":
    base = "https://glenrobson.github.io/iiif_stuff/zooniverse/partof"

    previous_step = 'with_id'
    this_step = 'partof'

    with open('../{}/manifest.json'.format(previous_step)) as json_file:
        manifest = json.load(json_file)
        for file in os.listdir("../{}".format(previous_step)): 
            if 'annoPage' in file and file.endswith('.json'):
                with open(os.path.join('../{}'.format(previous_step), file)) as json_file:
                    annoPage = json.load(json_file)
                    annoPage['id'] = annoPage['id'].replace(previous_step, this_step)

                    for anno in annoPage['items']:
                        origTarget = anno['target']
                        (canvasId, fragment) = origTarget.split('#')

                        anno['target'] = {
                            "type": "SpecificResource",
                            "source": {
                                  "id": canvasId,
                                  "type": "Canvas",
                                  "partOf": [{
                                       "id": manifest['@id'],
                                       "type": "Manifest",
                                  }]
                            },
                            "selector": {
                               "type": "FragmentSelector",
                               "conformsTo": "http://www.w3.org/TR/media-frags/",
                               "value": fragment
                             }
                        }

                    with open(file, 'w') as outfile:
                        json.dump(annoPage, outfile)

    # Update manifest annotation links to links in this directory
        for canvas in manifest['sequences'][0]['canvases']:
            if 'annotations' in canvas:
                canvas['annotations'][0]['id'] = canvas['annotations'][0]['id'].replace(previous_step, this_step)

        with open('manifest.json', 'w') as outfile:
            json.dump(manifest, outfile)
