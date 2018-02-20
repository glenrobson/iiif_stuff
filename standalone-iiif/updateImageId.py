#!/usr/bin/python

import json
import sys
import os
if __name__ == "__main__":

    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Usage:\n\tupdateImageId.py info.json [optional_replace_prefix] [image_prefix]")
        print ("Arg no = %s" % len(sys.argv))
        sys.exit(0)
    with open(sys.argv[1], 'r') as json_file:
        data = json.load(json_file)
        if len(sys.argv) == 3:
            data["@id"] = '%s%s' % (data["@id"], sys.argv[2])
        elif len(sys.argv) == 4:
            data["@id"] = data["@id"].replace(sys.argv[2],sys.argv[3])
        print (json.dumps(data,indent=4))

        with open('%s.new' % sys.argv[1], 'w') as out_file:
            json.dump(data,out_file,indent=4)

    os.rename('%s.new' % sys.argv[1], sys.argv[1])
