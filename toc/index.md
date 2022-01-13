# Looking at Table of Contents

It looks like there are two different ways of creating a table of contents in IIIF Version 2.0 of the presentation API. One that uses `members` and one that uses `ranges`. `members` was introduced in [Presentation 2.1](https://iiif.io/api/presentation/2.1/change-log/#14-allow-single-ordered-list-for-collection-and-range) and it looks like Mirador 2 only supports the use of `ranges` option not the `members`. The UV seems to support both.  

There are various examples below including:

 * the example from the training which doesn't work in Mirador 3 and the UV but does work in Mirador 2
 * Examples from Harry showing the `members` method and the `ranges` method
 * A live example from the Welcome Trust
 * A hierarchy with three levels using the `ranges` method which works on Mirador 2, Mirador 3 and the UV

## Example from the training
Latest version from training: https://training.iiif.io/iiif-bl-workshop/day-three/ranges/
 * [new_training_toc.json](https://glenrobson.github.io/iiif_stuff/toc/new_training_toc.json)
 * [UV](https://uv-v4.netlify.app/#?manifest=https://glenrobson.github.io/iiif_stuff/toc/new_training_toc.json)
 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://glenrobson.github.io/iiif_stuff/toc/new_training_toc.json)
 * [Miradro2](http://iiif.gdmrdigital.com/mirador/index.html)

Previous version from: https://training.iiif.io/iiif-bl-workshop/day-three/ranges/
 * [training-toc.json](https://iiif-test.github.io/BL-Nov-2021/manifests/training-toc.json)
 * Doesn't work, shows the introduction twice and only second one works: [UV](https://uv-v4.netlify.app/#?manifest=https://iiif-test.github.io/BL-Nov-2021/manifests/training-toc.json)
 * Same issue as above: [Mirador](https://projectmirador.org/embed/?iiif-content=https://iiif-test.github.io/BL-Nov-2021/manifests/training-toc.json)
 * Works in Mirador 2: [http://iiif.gdmrdigital.com/mirador/index.html](http://iiif.gdmrdigital.com/mirador/index.html)


```
"structures": [
        {
          "@id": "http://example.org/iiif/book1/range/r0",
          "@type": "sc:Range",
          "label": "Table of Contents",
          "members": [
                {
                  "@id": "http://example.org/iiif/book1/range/r1",
                  "@type": "sc:Range",
                  "label": "Introduction"
                }
          ]
        },
        {
              "@id": "http://example.org/iiif/book1/range/r1",
              "@type": "sc:Range",
              "label": "Introduction",
              "canvases": ["$YOUR_CANVAS_ID"]
        }
    ]
```    

##  Structures working with ranges (From Harry)
 * [manifest2.json](https://hwithington.github.io/IIIF-Training/manifests/manifest2.json)
 * [UV](https://uv-v4.netlify.app/#?manifest=https://hwithington.github.io/IIIF-Training/manifests/manifest2.json) 
 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://hwithington.github.io/IIIF-Training/manifests/manifest2.json)
 * Works in Mirador 2: [http://iiif.gdmrdigital.com/mirador/index.html](http://iiif.gdmrdigital.com/mirador/index.html)

TOC Structure:
 *  Intro - not shown at all in any of the viewers
   -  Act 1
      - Act 1 Scene 1
      - Act 1 Scene 2
      - Act 1 Scene 3
   - Act 2
      - Act 2 Scene 1
      - Act 2 Scene 2

```
structures": [

    {
        "@id": "http://example.org/iiif/book1/range/r0",
        "@type": "sc:Range",
        "label": "Intro",
        "viewingHint": "top",
        "ranges": [
            "http://example.org/iiif/book1/range/r1",
            "http://example.org/iiif/book1/range/r2",
            "http://example.org/iiif/book1/range/r8"
        ]
    },
    {
        "@id": "http://example.org/iiif/book1/range/r1",
        "@type": "sc:Range",
        "label": "Act 1",
        "ranges": [
            "http://example.org/iiif/book1/range/r3",
            "http://example.org/iiif/book1/range/r4",
            "http://example.org/iiif/book1/range/r5"
        ]
    },
    {
        "@id": "http://example.org/iiif/book1/range/r2",
        "@type": "sc:Range",
        "label": "Act 2",
        "ranges": [
            "http://example.org/iiif/book1/range/r6",
            "http://example.org/iiif/book1/range/r7"
        ]
    },
    {
        "@id": "http://example.org/iiif/book1/range/r3",
        "@type": "sc:Range",
        "label": "Act 1 Scene 1",
        "canvases": [
            "http://aae88280-7b83-4f04-a948-498e64b7cc60"
        ]
    },
    {
        "@id": "http://example.org/iiif/book1/range/r4",
        "@type": "sc:Range",
        "label": "Act 1 Scene 2",
        "canvases": [
            "http://6afb7742-37a5-4e91-8c76-01260b36a557"
        ]
    },
    ...
```    

## Structures working with members (From Harry) 
 * [manifest3.json](https://hwithington.github.io/IIIF-Training/manifests/manifest3.json)
 * [UV](https://uv-v4.netlify.app/#?manifest=https://hwithington.github.io/IIIF-Training/manifests/manifest3.json)
 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://hwithington.github.io/IIIF-Training/manifests/manifest3.json)
 * Doesn't work in Mirador 2: [http://iiif.gdmrdigital.com/mirador/index.html](http://iiif.gdmrdigital.com/mirador/index.html)

```
structures": [

    {
        "@id": "http://example.org/iiif/book1/range/r1",
        "@type": "sc:Range",
        "label": "Act 1",
        "members": [
            {
                "@id": "http://example.org/iiif/book1/range/r3",
                "@type": "sc:Range",
                "label": "Act 1 Scene 1",
                "canvases": [
                    "http://aae88280-7b83-4f04-a948-498e64b7cc60"
                ]
            },
            {
                "@id": "http://example.org/iiif/book1/range/r4",
                "@type": "sc:Range",
                "label": "Act 1 Scene 2",
                "canvases": [
                    "http://6afb7742-37a5-4e91-8c76-01260b36a557"
                ]
            },
            {
                "@id": "http://example.org/iiif/book1/range/r5",
                "@type": "sc:Range",
                "label": "Act 1 Scene 3",
                "canvases": [
                    "http://f93bc184-9299-4399-867d-5c393214fbc9"
                ]
            }
        ]
    },
    ...
```    

## Flat example from the Welcome Trust
 * [manifest.json](https://iiif.wellcomecollection.org/presentation/v2/b18035723)
 * [UV](http://universalviewer.io/examples/#?c=&m=&s=&cv=&manifest=https%3A%2F%2Fwellcomelibrary.org%2Fiiif%2Fb18035723%2Fmanifest&xywh=-1336%2C-197%2C5240%2C3936)
 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://iiif.wellcomecollection.org/presentation/v2/b18035723)   
 * Works in Mirador 2: [http://iiif.gdmrdigital.com/mirador/index.html](http://iiif.gdmrdigital.com/mirador/index.html)

```
"structures": [

    {
        "@id": "https://iiif.wellcomecollection.org/presentation/b18035723/ranges/LOG_0001",
        "@type": "sc:Range",
        "label": "Front Cover",
        "canvases": [
            "https://iiif.wellcomecollection.org/presentation/b18035723/canvases/b18035723_0001.JP2"
        ],
        "within": ""
    },
    {
        "@id": "https://iiif.wellcomecollection.org/presentation/b18035723/ranges/LOG_0003",
        "@type": "sc:Range",
        "label": "Title Page",
        "canvases": [
            "https://iiif.wellcomecollection.org/presentation/b18035723/canvases/b18035723_0004.JP2"
        ],
        "within": ""
    },
    {
        "@id": "https://iiif.wellcomecollection.org/presentation/b18035723/ranges/LOG_0002",
        "@type": "sc:Range",
        "label": "Back Cover",
        "canvases": [
            "https://iiif.wellcomecollection.org/presentation/b18035723/canvases/b18035723_0002.JP2"
        ],
        "within": ""
    }

],
```

## A hierarchy with three levels
 * [toc.json](https://glenrobson.github.io/iiif_stuff/toc/toc-example.json)
 * [UV](https://uv-v4.netlify.app/#?manifest=https://glenrobson.github.io/iiif_stuff/toc/toc-example.json)
 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://glenrobson.github.io/iiif_stuff/toc/toc-example.json)
 * Works in Mirador 2: [http://iiif.gdmrdigital.com/mirador/index.html](http://iiif.gdmrdigital.com/mirador/index.html)

Desired structure:

 * Table of Contents
   * Intro
     * Covers
     * Other pages
   * Criminals
     * Page 4
     * Upside down (page 3)


```
"structures": [
    {
        "@id": "http://example.org/range/root",
        "@type": "sc:Range",
        "label": "This range is not shown",
        "viewingHint": "top",
        "ranges": [
            "http://example.org/range/toc"
        ]
    },
    {
        "@id": "http://example.org/range/toc",
        "@type": "sc:Range",
        "label": "Table of Contents",
        "ranges": [
            "http://example.org/range/intro",
            "http://example.org/range/criminals"
        ]
    },
    {
        "@id": "http://example.org/range/intro",
        "@type": "sc:Range",
        "label": "Intro",
        "ranges": [
            "http://example.org/range/covers",
            "http://example.org/range/other_pages"
        ]
    },
    {
        "@id": "http://example.org/range/covers",
        "@type": "sc:Range",
        "label": "Covers",
        "canvases": [
            "https://damsssl.llgc.org.uk/iiif/2.0/4389767/canvas/4389768.json",
            "https://damsssl.llgc.org.uk/iiif/2.0/4389767/canvas/4389769.json"
        ]
    },
    {
        "@id": "http://example.org/range/other_pages",
        "@type": "sc:Range",
        "label": "Other Pages",
        "canvases": [
            "https://damsssl.llgc.org.uk/iiif/2.0/4389767/canvas/4389770.json"
        ]
    },
    {
        "@id": "http://example.org/range/criminals",
        "@type": "sc:Range",
        "label": "Criminals",
        "ranges": [
            "http://example.org/range/p4",
            "http://example.org/range/upside_down"
        ]
    },
    {
        "@id": "http://example.org/range/p4",
        "@type": "sc:Range",
        "label": "Page 4",
        "canvases": [
            "https://damsssl.llgc.org.uk/iiif/2.0/4389767/canvas/4389771.json"
        ]
    },        {
        "@id": "http://example.org/range/upside_down",
        "@type": "sc:Range",
        "label": "Upside down (page 3)",
        "canvases": [
            "https://damsssl.llgc.org.uk/iiif/2.0/4389767/canvas/4389770.json"
        ]
    }
]
```


