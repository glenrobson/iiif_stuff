# IIIF 3D Prototyping

This is a place for prototyping options for adding 3d to IIIF. They are meant to test out different methodologies to see if they fit the use cases required for 3d. 

A complete list can be seen in the [IIIF 3D stories use case](https://github.com/IIIF/iiif-3d-stories/issues)  repository but here are few of the base use cases:

 * [I want to show a 3d model in a IIIF viewer]() -- no use case
 * [Models from different repositories in a single space]() -- no use case, can we document the broken Vase use case or reconstructing a physical room with different objects?
 * [Place two different models into a single space](https://github.com/IIIF/iiif-3d-stories/issues/6)
 * [Save and share camera positions](https://github.com/IIIF/iiif-3d-stories/issues/5)
 * [Defining Initial View Position](https://github.com/IIIF/iiif-3d-stories/issues/4)
 * [Support Annotation](https://github.com/IIIF/iiif-3d-stories/issues/3)
 * [Consistent Unit Scale](https://github.com/IIIF/iiif-3d-stories/issues/2)

## Approaches

One of the first things we need to decide is how the 3d world meets IIIF. As discussed in the [3D Problem Space](IIIF3d_problem_space.pdf) presentation, the IIIF presentation API has a concept of a [Canvas](https://iiif.io/api/presentation/3.0/#53-canvas) which images and video are painted on to. A IIIF canvas is defined as:

"The Canvas represents an individual page or view and acts as a central point for assembling the different content resources that make up the display"

This is a core part of IIIF and for 3d to fit with IIIF we need to find a way for a canvas to support 3d. Currently IIIF canvas has three dimensions; a width, height and time. Three approaches have been discussed and links to prototypes and further discussions can be found below:

 * [2d first - paint a 3d object on to a 2d canvas](2d_first/)
 * [3d first - add a `z` dimension to the canvas](3d_first/)
 * Viewport as a canvas 
