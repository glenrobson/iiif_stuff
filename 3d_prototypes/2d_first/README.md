# 2D First Approach
[index](../)

This was first suggested on the call on the 9th of March 2021. The approach here is to leave the canvas with three dimensions and treat the 3d object as a discreet object which can be painted on to the canvas. The canvas would look as follows:

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

A full manifest example is available [here](manifest.json). This option would be enough to support the first use case of allowing a 3d Model as can be seen in the example below: 

<a href="Astronaut.html">
    <img src="Astronaut_on_canvas.png" alt="Demo showing the Astronaut 3d model on a 2d canvas"/>
</a>

