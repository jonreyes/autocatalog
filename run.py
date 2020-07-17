#! /usr/bin/env python3
import os
import requests
import glob

fruits = []
for file in glob.glob("supplier-data/descriptions/*.txt"):
    with open(file,"r") as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip())
        fruit = {}
        name = lines[0]
        fruit["name"] = name
        weight = int(lines[1].split(" ")[0])
        fruit["weight"] = weight
        description = lines[2]
        fruit["description"] = description
        image_name = os.path.basename(file).split(".")[0]+".jpeg"
        fruit["image_name"] = image_name
        fruits.append(fruit)
http = "http://"
ip = "34.66.48.248"
url = http+ip+"/fruits/"
for fruit in fruits:
    r = requests.post(url,data=fruit)
    print(r.text)


