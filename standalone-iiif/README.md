The `updateImageId.py allows you to update a static iiif implementation to be severed from a different directory. To add a prefix to an existing Id run:

```
./standalone-iiif/updateImageId.py json_file 'https://glenrobson.github.io/iiif/welsh_book/
```

where `https://glenrobson.github.io/iiif/welsh_book/` is the prefix to insert.

To replace part of the prefix run the command as follows:

```
./standalone-iiif/updateImageId.py json_file 'to_replace' 'https://glenrobson.github.io/iiif/welsh_book/
```
