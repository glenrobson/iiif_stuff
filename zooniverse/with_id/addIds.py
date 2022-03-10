#! /usr/bin/env python3

import json 
import os
from urllib import request

def loadJson(url):
    with request.urlopen(url) as data:
        return json.loads(data.read())

if __name__ == "__main__":
    base = "https://glenrobson.github.io/iiif_stuff/zooniverse/with_id"

    annoCount = 0
    for file in os.listdir("../split"): 
        if 'annoPage' in file and file.endswith('.json'):
            with open(os.path.join('../split', file)) as json_file:
                annoPage = json.load(json_file)
                annoPage['id'] = annoPage['id'].replace('split','with_id')

                for anno in annoPage['items']:
                    anno['id'] = "{}/{}".format(base, annoCount)
                    annoCount += 1

                with open(file, 'w') as outfile:
                    json.dump(annoPage, outfile)

    # Update manifest annotation links to links in this directory
    with open('../split/manifest.json') as json_file:
        manifest = json.load(json_file)
        for canvas in manifest['sequences'][0]['canvases']:
            if 'annotations' in canvas:
                canvas['annotations'][0]['id'] = canvas['annotations'][0]['id'].replace('split','with_id')

        with open('manifest.json', 'w') as outfile:
            json.dump(manifest, outfile)
