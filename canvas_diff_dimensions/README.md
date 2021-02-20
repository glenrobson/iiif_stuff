# Testing canvases of different sizes

There have been discussions on the [IIIF slack](https://iiif.slack.com/archives/C18FHBKAQ/p1612523135050500) regarding how canvases of different sizes should be shown in a 2 up view. This was originally a [UV issue](https://github.com/UniversalViewer/universalviewer/issues/761) but has highlighted an inconsistency between Mirador and the UV and the IIIF specification doesn't provide a solution.

## St Andrew's use case

The original use case from St Andrew's is the following manifest which has 4 images and the 2nd and 3rd image should be shown side by side in 2 up view. Currently the UV respects the sizes of the images in each canvas so doesn't scale the smaller canvas to match the larger manifest:

 * [Manifest](https://collections.st-andrews.ac.uk/manifest-test/manifest.json)
 * [UV](https://uv-v3.netlify.app/#?c=&m=&s=&cv=&manifest=https://collections.st-andrews.ac.uk/manifest-test/manifest.json)

Mirador currently does what St Andrew's want and scales the smaller canvas to match the larger canvas:

 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://collections.st-andrews.ac.uk/manifest-test/manifest.json)

## Uniform canvas heights
One way to solve this issue is to ensure both canvases have the same height. As shown in the [Image and Canvas with Differing Dimensions](https://iiif.io/api/cookbook/recipe/0004-canvas-size/) recipe, if an image is placed on a canvas which has bigger dimensions than the image it should be scaled up. In the manifest below the second canvas has been enlarged so the height is the same on canvas 2 and 3. The size of the 3rd image is left unchanged and the viewer should scale it.  

 * [Manifest](https://glenrobson.github.io/iiif_stuff/canvas_diff_dimensions/manifest-normalised.json)

The UV currently doesn't respect the canvas dimensions due to issue [#778](https://github.com/UniversalViewer/universalviewer/issues/778) but if it did it should sort out the lack of alignment:

 * [UV](https://uv-v3.netlify.app/#?c=&m=&s=&cv=&manifest=https://glenrobson.github.io/iiif_stuff/canvas_diff_dimensions/manifest-normalised.json)

Mirador looks like it respects the canvas coordinates although it maybe scaling the image as mentioned previously.  
 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://glenrobson.github.io/iiif_stuff/canvas_diff_dimensions/manifest-normalised.json)

## Variable height use case
One downside of the Mirador implementation is that it assumes the Manifest provider wants to scale the smaller canvas but this might not be appropriate. In the following manuscript example the 3rd image is much smaller than its facing page but it would still be valid to have the sequence as paged. This might also happen if there are pullouts or other unexpected page sizes in a book or manuscript.  

 * [Manifest](https://glenrobson.github.io/iiif_stuff/canvas_diff_dimensions/manifest-different.json)

In this case the UV shows the two images but doesn't scale up the smaller image (note I was careful to match the dimensions of the 3rd canvas and 3rd image to avoid [#778](https://github.com/UniversalViewer/universalviewer/issues/778)):

 * [UV](https://uv-v3.netlify.app/#?c=&m=&s=&cv=&manifest=https://glenrobson.github.io/iiif_stuff/canvas_diff_dimensions/manifest-different.json)

With Mirador it scales up the smaller canvas and doesn't look correct for this use case:
 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://glenrobson.github.io/iiif_stuff/canvas_diff_dimensions/manifest-different.json)

This is a slightly contrived case as you can see the original image was the same size as the facing page. For manifest above I cutout the manuscript fragment and used a static image in the manifest.

![Original Image](https://damsssl.llgc.org.uk/iiif/2.0/image/4396879/full/512,/0/default.jpg)
