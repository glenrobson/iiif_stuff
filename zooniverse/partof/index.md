# Zooniverse Testing - partOf

I created [this script](https://github.com/glenrobson/iiif_stuff/blob/master/zooniverse/partof/addPartOf.py) to add a link from the annotation to the Manifest. This script uses the annotations generated in the [add ID step](../with_id). 

Adding a link from the annotation to the Manifest can be really helpful as it allows annotation consumers to get access to the image underneath the annotation as it can't use the canvas id because it doesn't necessarily resolve. The link to the manifest is added to the target and the original annotation looked like this:

```
{
    "id": "https://glenrobson.github.io/iiif_stuff/zooniverse/with_id/79",
    "type": "Annotation",
    "motivation": "tagging",
    "body": {
        "format": "text/plain",
        "language": "en",
        "type": "TextualBody",
        "value": "Rochester, or, King Charles the Second's Merry Days."
    },
    "target": "https://api.bl.uk/metadata/iiif/ark:/81055/vdc_100022589176.0x0001c3#xywh=570,1472,1814,314"
}
```

and with the link back to the manifest it looks like:

```
{
    "id": "https://glenrobson.github.io/iiif_stuff/zooniverse/with_id/79",
    "type": "Annotation",
    "motivation": "tagging",
    "body": {
        "type": "TextualBody",
        "format": "text/plain",
        "language": "en",
        "value": "Rochester, or, King Charles the Second's Merry Days."
    },
    "target": {
        "type": "SpecificResource",
        "source": {
            "id": "https://api.bl.uk/metadata/iiif/ark:/81055/vdc_100022589176.0x0001c3",
            "type": "Canvas",
            "partOf": [{
                    "id": "https://api.bl.uk/metadata/iiif/ark:/81055/vdc_100022589176.0x000002/manifest.json",
                    "type": "Manifest"
            }]
        },
        "selector": {
            "type": "FragmentSelector",
            "conformsTo": "http://www.w3.org/TR/media-frags/",
            "value": "xywh=570,1472,1814,314"
        }
    }
}
```

Looking at the edited [manifest](manifest.json) in Mirador it seems to still work OK:

<div id="mirador" style="width: 100%; height: calc(100vh - 3px); position: relative;"></div>
<script type='text/javascript' src='https://unpkg.com/mirador@latest/dist/mirador.min.js'></script>
<script type="text/javascript">
      var miradorInstance = Mirador.viewer({
        id: 'mirador',
        windows: [
            {
                manifestId: 'https://glenrobson.github.io/iiif_stuff/zooniverse/partof/manifest.json',
                sideBarPanel: 'annotations',
                sideBarOpen: true
            }
        ],
      });
</script>      

This type of annotation list should also work with another IIIF tool called [Annona](https://ncsu-libraries.github.io/annona/) which is really good for presenting your annotations. Unfortunately it doesn't look like it currently supports this form of annotation. Annona did support the version 2 version of this annotation structure and it means Annona can work with just the annotation page without also being supplied with the manifest. 

<script src="https://ncsu-libraries.github.io/annona/dist/annona.js"></script>
<link rel="stylesheet" type="text/css" href="https://ncsu-libraries.github.io/annona/dist/annona.css">

<div id="storyboard">
<iiif-storyboard annotationlist='https://glenrobson.github.io/iiif_stuff/zooniverse/partof/annoPage-0.json'></iiif-storyboard>
</div>

The annotation pages with part of included in the annotation:

 * [annoPage-0.json](annoPage-0.json)
 * [annoPage-1.json](annoPage-1.json)
 * [annoPage-2.json](annoPage-2.json)
 * [annoPage-3.json](annoPage-3.json)
 * [annoPage-4.json](annoPage-4.json)
 * [annoPage-5.json](annoPage-5.json)
 * [annoPage-6.json](annoPage-6.json)
 * [annoPage-7.json](annoPage-7.json)
 * [annoPage-8.json](annoPage-8.json)
 * [annoPage-9.json](annoPage-9.json)
 * [annoPage-10.json](annoPage-10.json)
 * [annoPage-11.json](annoPage-11.json)
 * [annoPage-12.json](annoPage-12.json)
 * [annoPage-13.json](annoPage-13.json)
 * [annoPage-14.json](annoPage-14.json)
 * [annoPage-15.json](annoPage-15.json)
 * [annoPage-16.json](annoPage-16.json)
 * [annoPage-17.json](annoPage-17.json)
 * [annoPage-18.json](annoPage-18.json)
 * [annoPage-19.json](annoPage-19.json)
 * [annoPage-20.json](annoPage-20.json)
 * [annoPage-21.json](annoPage-21.json)
 * [annoPage-368.json](annoPage-368.json)

