# 3D Prototyping

Example manifest [here](https://glenrobson.github.io/iiif_stuff/3d_prototypes/manifest.json)

## Aims

 * Show that it is possible and useful to link multiple models from distributed places into single canvas/scene
 * Find out where standards are missing and IIIF extensions are needed
 * Prototype clients
 * See if use cases can be achieved 

In some ways this work is similar to early prototyping in the AV work like [this example](https://tomcrane.github.io/fire/) from Tom Crane.

## Questions

 * Is it OK to have scene dimensions e.g. width, height, depth
 * 3d `type` from https://www.w3.org/TR/annotation-model/#Classes currently either (Dataset, Image, Video, Sound or Text)
 * Format?
 * Does the target make sense:

```https://glenrobson.github.io/iiif_stuff/3d_prototypes/scene/1?xyzwhd=100,100,100,500,500,500```

Allows you to scale a model into the scene. Note z and d (for depth) don't exist in [media-frags](https://www.w3.org/TR/media-frags/) specifications. 

