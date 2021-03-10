# 2D First Approach
[index](../)

This was first suggested on the call on the 9th of March 2021. The approach here is to leave the canvas with three dimensions and treat the 3d object as a discreet object which can be painted on to the canvas. The canvas would look as follows:

[manifest.json](manifest.json)
```
{
  "id": "https://glenrobson.github.io/iiif_stuff/3d_prototypes/scene/1",
  "type": "Canvas",
  "height": 1000,
  "width": 1000,
  "items": [
    {
      "id": "https://glenrobson.github.io/iiif_stuff/3d_prototypes/annotations",
      "type": "AnnotationPage",
      "items": [
        {
          "id": "https://glenrobson.github.io/iiif_stuff/3d_prototypes/annotations/1",
          "type": "Annotation",
          "motivation": "painting",
          "body": {
            "id": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
            "type": "Dataset",
            "format": "model/gltf-binary"
          },
          "target": "https://glenrobson.github.io/iiif_stuff/3d_prototypes/scene/1"
        }
      ]
    }
  ]
}
```

In this example the 3d model is painted onto the canvas and fills the full width and height of the canvas. The canvas dimensions are arbitrary in this example but are required by IIIF.  This type of manifest could be shown in a viewer like the following demo: 

<a href="Astronaut.html">
    <img src="Astronaut_on_canvas.png" alt="Demo showing the Astronaut 3d model on a 2d canvas" style="width: 400px; display: block; margin-left: auto; margin-right: auto;"/>
</a>

and would solve the first use case of allowing a IIIF viewer to show a 3d model. 

## Models from different repositories in a single space

It could in a way handle brining together two models from different locations. This could be achieved in a similar way to how IIIF can draw images from different repositories. In the following example the canvas has two annotations one for each model. The first model is the Astronaut one shown earlier and the second model is stored locally but is downloaded from [SketchFab](https://skfb.ly/6SWEH). The difficulty is where to target the two models on the canvas. This example draws the two models side by side on the canvas. See the [example manifest](side_by_side.json) and the demo below:

<a href="side_by_side.html">
    <img src="side_by_side.png" alt="Demo showing the 2 3d models on a single 2d canvas" style="width: 400px; display: block; margin-left: auto; margin-right: auto;"/>
</a>

