# IIIF Implementation Map with navPlace

So during the [IIIF Online Conference](https://iiif.io/event/2022/online-meeting/) - Maps session Bryan challenged us to move the [Implementation map](https://iiif.io/community/map/) to use IIIF. It might be possible to download the locations but due to time constraints I'm going to limit it to consortium members who are handily represented with Geo location and images in Wikidata. Using this query:

https://query.wikidata.org/#%23Cats%0ASELECT%20%3Fitem%20%3FitemLabel%20%3Flocation%20%3Fimage%20%3Flogo%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20wdt%3AP463%20wd%3AQ35677307.%20%0A%20%20optional%20%7B%3Fitem%20wdt%3AP625%20%3Flocation%7D%20.%0A%20%20optional%20%7B%3Fitem%20wdt%3AP18%20%3Fimage%7D.%0A%20%20optional%20%7B%3Fitem%20wdt%3AP154%20%3Flogo%7D%20.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%20%23%20Helps%20get%20the%20label%20in%20your%20language%2C%20if%20not%2C%20then%20en%20language%0A%7D

```
# IIIF Consortium members with image or logo
SELECT ?item ?itemLabel ?location ?image ?logo
WHERE 
{
  ?item wdt:P463 wd:Q35677307. 
  optional {?item wdt:P625 ?location} .
  optional {?item wdt:P18 ?image}.
  optional {?item wdt:P154 ?logo} .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # Helps get the label in your language, if not, then en language
}
```

To get a CSV of places with at least a logo image or a picture of the institution. I can then use the new [iiif-prezi3](https://github.com/iiif-prezi/iiif-prezi3) library recently released to build up a manifest with a canvas per institution with an associated image and navPlace. The ugly code for this is [here](createManifest.py).

The resulting manifest is at [manifest.json](manifest.json) and you can see this in the NavPlace viewer [here](https://centerfordigitalhumanities.github.io/navplace-viewer/?iiif-content=https://glenrobson.github.io/iiif_stuff/consortium_navplace/manifest.json).



