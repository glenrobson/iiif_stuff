# 3D Prototyping

Example manifest [here](https://glenrobson.github.io/iiif_stuff/3d_prototypes/manifest.json)

## Questions

 * Is it OK to have scene dimensions e.g. width, height, depth
 * 3d `type` from https://www.w3.org/TR/annotation-model/#Classes currently either (Dataset, Image, Video, Sound or Text)
 * Format?
 * Does the target make sense:

```https://glenrobson.github.io/iiif_stuff/3d_prototypes/scene/1?xyzwhd=100,100,100,500,500,500```

Allows you to scale a model into the scene. Note z and d (for depth) don't exist in [media-frags](https://www.w3.org/TR/media-frags/) specifications. 

