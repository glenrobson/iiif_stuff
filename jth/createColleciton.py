import sys
from iiif_prezi3 import Collection, ManifestRef


collection = Collection(id="https://glenrobson.github.io/iiif-stuff/jth/collection.json",
                        label="NLW John Thomas Collection")

with open(sys.argv[1]) as lines:
    for line in lines:

        manifest = ManifestRef(id="https://iiif.io/api/cookbook/recipe/0230-navdate/navdate_map_2-manifest.json",
                           type="Manifest")
        collection.add_item(manifest)                   


print(collection.jsonld())        
