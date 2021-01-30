# Face detection

This uses the excellent [Annotorious](https://recogito.github.io/annotorious/) annotation tool from Recogito in combination with [face-api.js](https://itnext.io/face-api-js-javascript-api-for-face-recognition-in-the-browser-with-tensorflow-js-bcc2a6c4cf07) to detect faces in IIIF images in the browser. 

## Implementation Notes

[Annotorious](https://recogito.github.io/annotorious/) integrates into [Openseadragon](https://openseadragon.github.io/) which is one of the IIIF Image API viewers. 

The face-api.js uses a JavaScript version of tenserflow and in this version a Single Shot Multibox Detector machine learning model to identify faces and return x,y,width,heigh in the image. My code then converts them to W3C annotations and passes them to Annotorious to draw them on to Openseadragon. 

## Try a IIIF Image

Try your own IIIF Image URL: 
<form action="demo.html" method="GET">
<div class="form-group">
<label for="image_api">IIIF Image URL:</label>
<input type="text" id="image_api" name="iiif-content" size="70"/>
<button type="submit">View</button>
</div>    
</form>

## Examples

This isn't a perfect solution but does work on the following images:

 * [National Library of Wales, Photograph by John Thomas](demo.html?iiif-content=https://damsssl.llgc.org.uk/iiif/2.0/image/4670355) - ([Image at NLW](https://viewer.library.wales/4670355))
 * [National Library of Wales, Photograph by Geoff Charles - multiple people in photo](demo.html?iiif-content=https://damsssl.llgc.org.uk/iiif/2.0/image/1459052) - ([Image at NLW](https://viewer.library.wales/1459048))

The results for the following are not so great:

 * [Group portrait from Library of The Jewish Theological Seminary](demo.html?iiif-content=https://media.jhn.ngo/iiif/2/DC_JTSA:oai_jts_jts_38225:38225_PNT_G_01880.tif.tiff) - ([Image in Europeana](https://www.europeana.eu/en/item/232/https___digitalcollections_jtsa_edu_islandora_object_jts_3A38225_datastream_TN_view__5BGroup_20portrait_5D__jpg))
 * [National Library of Wales, Photograph by Geoff Charles - multiple people some not looking at camera](demo.html?iiif-content=https://damsssl.llgc.org.uk/iiif/2.0/image/1459049) - ([Image at NLW](https://viewer.library.wales/1459048))
