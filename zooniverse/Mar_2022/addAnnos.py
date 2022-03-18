#! /usr/bin/env python3

import json 
from urllib import request
import os
import base64

def loadJson(url):
    with request.urlopen(url) as data:
        return json.loads(data.read())

# just a check to make sure that annoPages only link to one canvas 
def checkOnlyOneCanvasInAnnoPage(annoPage):
    canvases = []
    for anno in annoPage['items']:
        canvas = anno['target']['source']['id']
        if canvas not in canvases:
            canvases.append(canvas)

    return len(canvases) < 2

def addManifest(manifests, manifestURL):
    manifest = loadJson(manifestURL)
    manifests[manifestURL] = manifest

def addAnnosToCanvas(manifest, canvasID, annoPageURL):
    canvasNo = 0
    for canvas in manifest['sequences'][0]['canvases']:
        print ('Adding annotations to canvas no: {}'.format(canvasNo))

        if canvas['@id'] == canvasID:
            # Add link to manifest pointing to annotation page
            canvas['annotations'] = [{
                "id": annoPageURL, # add the URL to the annotation page to the manifest
                "type": "AnnotationPage"
            }]
            break

        canvasNo += 1 

def processAnnoPage(manifests, annoPageURL): 
    print ('Proccessing {}'.format(annoPageURL))
    annoPage = loadJson(annoPageURL)

    if checkOnlyOneCanvasInAnnoPage(annoPage): 
        if 'items' in annoPage and len(annoPage['items']) > 0:
            target = annoPage['items'][0]['target']

            canvas = target['source']['id']
            manifestURL = target['source']['partOf']['id']

            if manifestURL not in manifests:
                addManifest(manifests, manifestURL)
            
            manifest = manifests[manifestURL]
            # Add anno page to canvas
            addAnnosToCanvas(manifest, canvas, annoPageURL)
        else:
            print ('Annotation page is empty')
    else:
        print ('Anno page {} contains more than one canvas'.format(annoPageURL))

    if 'next' in annoPage:
        processAnnoPage(manifests, annoPage['next']['id'])
    

if __name__ == "__main__":
    base = "https://glenrobson.github.io/iiif_stuff/zooniverse/Mar_2022"

    tAnnoCollection = loadJson('https://zooniverse.github.io/iiif-annotations/annotations/titles.json')

    # Place to store downloaded Manifests that will be updated
    manifests = {
    }

    processAnnoPage(manifests, tAnnoCollection['first']['id'])

    # Write out the manifest with annotation links to file
    for manifestURL in manifests:
        splitManifestURL = manifestURL.split("/")
        # This will only work with BL manifest URLs which have the id before tha manifest e.g:
        # https://api.bl.uk/metadata/iiif/ark:/81055/vdc_100022589176.0x000002/manifest.json
        filename = splitManifestURL[len(splitManifestURL) - 2] + ".json"
        print ('Writing out {}'.format(filename))
        with open(filename, 'w') as outfile:
            json.dump(manifests[manifestURL], outfile)
