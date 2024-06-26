## ALTO to Annotation list

This XSLT converts an ALTO xml document to an annotation lists for use with a IIIF manifests. To link to an annotation list from a manifest add the following in the related canvas:

```
"otherContent": [
    {
        "@id": "http://dams.llgc.org.uk/iiif/2066058/annotation/list.json",
        "@type": "sc:AnnotationList"
    }
]
```

**Note** this XSLT produces word level annotations. If you prefer line level annotations see the comment in the XSLT.

The required parameters are:

 * **annoURI** this should be a resolvable URI to the generated annotation list.
 * **xRatio,yRatio** these are the ratios to divide the coordinates by if the IIIF image is smaller than the source image the ALTO was generated from. If the IIIF image and ALTO image are the same size use ```1```.
 * **canvasURI** this is the page level canvasURI and must match the canvas ID in the manifest.

You can also optionally supply:
 * **manifestURI** if this is supplied it will add a ```within``` field to all of the annotations pointing to the manifest. This is useful as the canvas URI isn't necessarily resolvable so being able to get the manifest that contains the canvas allows users of the annotation to display the image as well as the annotation. If the viewer is starting from the Manifest (e.g. with Mirador) this within isn't used.

To run this from the command line you can run:

```
xsltproc --stringparam annoURI "http://localhost:8887/altoAnnotations.json" --stringparam xRatio 1 --stringparam yRatio 1  --stringparam canvasURI "http://07ae9a4f-5e65-4ecd-9796-7f682e7e0b37" annotationListNoArt.xsl /Users/gmr/Downloads/CAVA_TS_1371_5097_0008_002_alto.xml > altoAnnotations.json
```
 * [annotationListNoArt.xsl - Open Annotations IIIF v2](annotationListNoArt.xsl)
 * [alto2annosv3.xsl - Web Annotations IIIF v3](alto2annosv3.xsl)