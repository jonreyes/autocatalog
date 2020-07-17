#!/usr/bin/env python3
import os
from PIL import Image
import glob

for file in glob.glob("supplier-data/images/*.tiff"):
    im = Image.open(file)
    im = im.convert("RGB")
    im = im.resize((600,400))
    out = file.split(".")[0]
    out = out + ".jpeg"
    im.save(out,"JPEG")

