# Transform Annotations from Open Annotations to Web Annotations

This code is specifically targeted to converting Europeana Newspapers Annotations but maybe useful for others.

Example version 2.0 Annotation list:

https://iiif.europeana.eu/presentation/9200355/BibliographicResource_3000096302513/annopage/1

Note this uses a single full text file and links into it using character positions. For example:

```
{
    "@id" : "https://data.europeana.eu/annotation/9200355/BibliographicResource_3000096302513/20b3b1f4cb15f062e53fd50d584d66ff",
    "@type" : "oa:Annotation",
    "motivation" : "sc:painting",
    "dcType" : "Word",
    "resource" : {
      "@id" : "https://www.europeana.eu/api/fulltext/9200355/BibliographicResource_3000096302513/8c6abaa8b05a33a93526a8f6d0411bf5#char=0,2"
    },
    "on" : [ "https://iiif.europeana.eu/image/2YMIN6YXMQ6COVM5AO2XKB5KMCKPMT2YKEKNMAGHVRBIHOOY4AVA/presentation_images/9340afd0-ffe2-11e5-b68d-fa163e60dd72/node-2/image/SBB/Berliner_Tageblatt/1925/02/16/0/F_SBB_00001_19250216_054_079_0_001/full/full/0/default.jpg#xywh=182,476,59,43" ]
},
```

As this in use for a 3.0 recipe I am going to make the following changes:

 * Pull out only the word annotations
 * Turn the body of the annotation into a plan text body
 * Convert the image annotation to a IIIF Canvas

The manifest for this resource is part of the IIIF Cookbook and is available at:

https://preview.iiif.io/cookbook/0068-newspaper/recipe/0068-newspaper/newspaper_issue_1-manifest.json

The canvas for this page is:

 * https://iiif.europeana.eu/presentation/9200355/BibliographicResource_3000096302513/canvas/p1
