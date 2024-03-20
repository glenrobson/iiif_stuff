# Viewing Hint

Looking at examples of viewing hint to see how they work in different viewers. The different viewingHint options are definied in the presentation API [here](https://iiif.io/api/presentation/2.1/#viewinghint). Note there is no default in version 2 of the specification. V3 specifies individuals as the default. 

It looks like the UV defaults to `paged` for all viewingHints apart from Continuous. There is an issue on the [UV github](https://github.com/UniversalViewer/universalviewer/issues/872) to fix this and it has been fixed in the dev version.

## No viewingHint

Example from the National Library of Wales:

 * [Manifest](https://glenrobson.github.io/iiif_stuff/viewingHint/no-hint.json)
 * [Universal Viewer 4](https://uv-v4.netlify.app/#?manifest=https://glenrobson.github.io/iiif_stuff/viewingHint/no-hint.json)
 * [Universal Viewer 3](https://uv-v4.netlify.app/#?manifest=https://glenrobson.github.io/iiif_stuff/viewingHint/no-hint.json)
 * [Universal Viewer Dev](https://www.universalviewer.dev/#?iiifManifestId=https://glenrobson.github.io/iiif_stuff/viewingHint/no-hint.json)
 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://glenrobson.github.io/iiif_stuff/viewingHint/no-hint.json)

## Individuals

Example from the National Library of Wales:

 * [Manifest](https://glenrobson.github.io/iiif_stuff/viewingHint/photos.json)
 * [Universal Viewer 4](https://uv-v4.netlify.app/#?manifest=https://glenrobson.github.io/iiif_stuff/viewingHint/photos.json)
 * [Universal Viewer 3](https://uv-v4.netlify.app/#?manifest=https://glenrobson.github.io/iiif_stuff/viewingHint/photos.json)
 * [Universal Viewer Dev](https://www.universalviewer.dev/#?iiifManifestId=https://glenrobson.github.io/iiif_stuff/viewingHint/photos.json)
 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://glenrobson.github.io/iiif_stuff/viewingHint/photos.json)

## Paged

Example from Stanford:

 * [Manifest](https://glenrobson.github.io/iiif_stuff/viewingHint/book.json)
 * [Universal Viewer 4](https://uv-v4.netlify.app/#?manifest=https://glenrobson.github.io/iiif_stuff/viewingHint/book.json)
 * [Universal Viewer 3](https://uv-v4.netlify.app/#?manifest=https://glenrobson.github.io/iiif_stuff/viewingHint/book.json)
 * [Universal Viewer Dev](https://www.universalviewer.dev/#?iiifManifestId=https://glenrobson.github.io/iiif_stuff/viewingHint/book.json)
 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://glenrobson.github.io/iiif_stuff/viewingHint/book.json)

## Continuous

Example from the University of Edinburgh 

 * [Manifest](https://librarylabs.ed.ac.uk/iiif/manifest/mahabharataFinal.json)
 * [Universal Viewer 4](https://uv-v4.netlify.app/#?manifest=https://librarylabs.ed.ac.uk/iiif/manifest/mahabharataFinal.json)
 * [Universal Viewer 3](https://uv-v4.netlify.app/#?manifest=https://librarylabs.ed.ac.uk/iiif/manifest/mahabharataFinal.json)
 * [Universal Viewer Dev](https://www.universalviewer.dev/#?iiifManifestId=https://librarylabs.ed.ac.uk/iiif/manifest/mahabharataFinal.json)
 * [Mirador](https://projectmirador.org/embed/?iiif-content=https://librarylabs.ed.ac.uk/iiif/manifest/mahabharataFinal.json)