# Zooniverse Testing - dates

I created [this script](https://github.com/glenrobson/iiif_stuff/blob/master/zooniverse/dates/addAnnos.py) which will process all of the annotations from the [dates annotation collection](https://zooniverse.github.io/iiif-annotations/annotations/dates.json). It will:

 * Download any manifests it finds
 * and add a link to the AnnotationPage to each canvas.
 * Follow the `next` link to the next AnnotationPage
 * Where it finds a valid date it will create the following annotation body:

```
"body": {
    "format": "text/html",
    "language": "en",
    "type": "TextualBody",
    "value": "<time datetime=\"1819-02-02\">February, 02 1819</time>"
},
```

The [manifest](vdc_100022589176.0x000002.json) and [example annotation page](0.json):

<div id="mirador" style="width: 100%; height: calc(100vh - 3px); position: relative;"></div>
<script type='text/javascript' src='https://unpkg.com/mirador@latest/dist/mirador.min.js'></script>
<script type="text/javascript">
      var miradorInstance = Mirador.viewer({
        id: 'mirador',
        windows: [
            {
                manifestId: 'https://glenrobson.github.io/iiif_stuff/zooniverse/dates/vdc_100022589176.0x000002.json',
                sideBarPanel: 'annotations',
                sideBarOpen: true
            }
        ],
      });
</script>      

<br/>

Thanks to the fix from [dnoneill](https://github.com/NCSU-Libraries/annona/issues/35) it also works in [Annona](https://ncsu-libraries.github.io/annona/) which is really good for presenting your annotations. 

<script src="https://ncsu-libraries.github.io/annona/dist/annona.js"></script>
<link rel="stylesheet" type="text/css" href="https://ncsu-libraries.github.io/annona/dist/annona.css">

<div id="storyboard">
<iiif-storyboard annotationlist='https://glenrobson.github.io/iiif_stuff/zooniverse/dates/0.json'></iiif-storyboard>
</div>

