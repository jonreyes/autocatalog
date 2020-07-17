#!/usr/bin/env python3
import os
import requests
import glob
http = "http://"
ip = "35.226.112.225"
url = http+ip+"/upload/"
for file in glob.glob("supplier-data/images/*.jpeg"):
    file = os.path.realpath(file)
    with open(file,"rb") as f:
        r = requests.post(url, files={"file":f})
