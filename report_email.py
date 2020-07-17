#!/usr/bin/env python3
#! /usr/bin/env python3
import os
import requests
import glob
import reports
import datetime
import emails

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
        fruits.append(fruit)
paragraph = []
for fruit in fruits:
    f = []
    f.append("name: "+fruit["name"])
    f.append("weight: "+str(fruit["weight"])+" lbs")
    f.append("")
    paragraph.append("\n".join(f))
paragraph = "\n".join(paragraph)
paragraph = paragraph.replace("\n","<br/>")
attachment = "/tmp/processed.pdf"
date = datetime.datetime.now()
date = date.strftime("%x")
title = "Processed Update on "+date
reports.generate(attachment,title,paragraph)
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get("USER"))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
message = emails.generate(sender, receiver, subject, body, attachment)
emails.send(message)
