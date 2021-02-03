# Use non IIIF Images in a Manifest

It has been possible to use non-IIIF images in a Manifest since the beginning of IIIF but the viewer support has only come into place in the last year or so. When I talk about a Non IIIF image, this is something like:

 * [https://fixtures.iiif.io/images/Glen/photos/gottingen.jpg](https://fixtures.iiif.io/images/Glen/photos/gottingen.jpg)

Which is just a straight jpg like any other image on the web. To add this to a manifest you create a canvas in the following form:

```
{
    "@id": "http://example.com/canvas/2",
    "@type": "sc:Canvas",
    "label": "Static Image",
    "height": 3024,
    "width": 4032,
    "images": [
        {
            "@id": "http://example.com/canvas/2/annotation/1",
            "@type": "oa:Annotation",
            "motivation": "sc:painting",
            "resource": {
                "@id": "https://fixtures.iiif.io/images/Glen/photos/gottingen.jpg",
                "@type": "dctypes:Image",
                "format": "image/jpeg",
                "height": 3024,
                "width": 4032
            },
            "on": "http://example.com/canvas/2"
        }
    ]
}
```

The parts that you need to edit in the code above is the references to `height` and `width` which should match the image you are using. Then replace the `resoure/@id` with the URL to your image. This is enough to create a canvas with a non IIIF image and the manifest can be annotated just like any other manifest. See the links below to see this in action:

__note:__ the second canvas in this example is a IIIF image so you can see the difference between a IIIF Image and a Non IIIF Image. 

 * [manifest2.json](https://glenrobson.github.io/iiif_stuff/simple_images/manifest2.json)
 * [Manifest in the Universal Viewer](https://uv-v3.netlify.app/#?c=&m=&s=&cv=&manifest=https://glenrobson.github.io/iiif_stuff/simple_images/manifest2.json)
 * [Manifest in Mirador3](https://projectmirador.org/embed/?iiif-content=https://glenrobson.github.io/iiif_stuff/simple_images/manifest2.json)
