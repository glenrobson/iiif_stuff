import sys
from iiif_prezi3 import Collection, ManifestRef


collection = Collection(id="https://glenrobson.github.io/iiif-stuff/jth/collection.json",
                        label="NLW John Thomas Collection")

with open(sys.argv[1]) as lines:
    for line in lines:

        manifest = ManifestRef(id=f"https://damsssl.llgc.org.uk/iiif/2.0/{line.rstrip()}/manifest.json",
                           type="Manifest")
        collection.add_item(manifest)                   


print(collection.jsonld())        
