#!/usr/bin/env python3 

import sys 
import json
from urllib import request

canvasHash = {}
def findCanvasId(manifest, imageId):
    if imageId in canvasHash:
        return canvasHash[imageId]
    else:
        canvas_id = None
        for canvas in manifest['items']:
            for annoPages in canvas['items']:
                for annos in annoPages['items']:
                    for services in annos['body']['service']:
                        print ('Checking {} against {}'.format(services['id'], imageId))
                        if services['id'] == imageId:
                            canvas_id = canvas['id']
                
        if canvas_id:     
            canvasHash[imageId] = canvas_id
        return canvas_id    
    return None            

urlText = {}    
def getText(uri):
    url = uri.split('#')[0]
    if url in urlText:
        (lang, text) = urlText[url]
    else:    
        print ('Getting {}'.format(url))
        with request.urlopen(url) as url_handle:
            annotation = json.loads(url_handle.read().decode('utf-8', 'ignore').encode('utf-8'))
        text = annotation['value']
        if 'language' in annotation:
            lang = annotation['language']
        else:
            lang = 'none'
        urlText[url] = (lang, text)
    
    addressStr = uri.split('#')[1].replace('char=','')
    address = [ int(addressStr.split(',')[0]), int(addressStr.split(',')[1]) ]
    print ('got {} from {}'.format("".join(text[address[0]: address[1]]), addressStr))
    return (lang, text[address[0]: address[1]])

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage\n\t{} 'anno_url' 'manifest' 'output_filename'".format(sys.argv[0]))
        sys.exit(-1)
    with request.urlopen(sys.argv[1]) as url:
        inputAnnoList = json.loads(url.read().decode())
    with request.urlopen(sys.argv[2]) as url:
        manifest = json.loads(url.read().decode())

    outputAnnoList = {
        "@context": "http://iiif.io/api/presentation/3/context.json",
        "id": "{{ id.url }}",
        "type": "AnnotationPage",
        "items": []
    }    

    for annotation in inputAnnoList['resources']:
        # Only interested in word annotations for now
        if annotation['dcType'] == "Word":
            newAnno = {
                'id': annotation['@id'],
                'type': 'Annotation',
                'motivation': 'supplementing',
                'body': {
                    "type" : "TextualBody",
                    "format" : "text/plain",
                },
                'target': ''
            }
            # Convert annotation ID into canvas id
            if 'on' in annotation:
                imageId = '/'.join(annotation['on'][0].split('/')[:-4])
                canvas_id  = findCanvasId(manifest, imageId)
                print ('{} to {}'.format(imageId, canvas_id))
                newAnno['target'] = canvas_id + "#" + annotation['on'][0].split('#')[1]
            else:
                print ('missing target in {} '.format(annotation['@id']))

            (newAnno['body']['language'],newAnno['body']['value']) = getText(annotation['resource']['@id'])
            
            outputAnnoList['items'].append(newAnno)
    with open(sys.argv[3], 'w') as outputFile:
        json.dump(outputAnnoList, outputFile, indent=4)
