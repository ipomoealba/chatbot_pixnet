#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open("../data/raw_data/2013：银魂 完结篇 永远的万事屋.ass", "r") as f:
    start = False
    with open("../data/yml/gintama.yml", "w+") as f1:
        f1.write("categories:\n- keywords\nconversations:")
    #  print(f.read())
    back = False
    for line in f.readlines():
        #  if "Events" in line:
            #  start = True
        #  if start:
        print(line.split(","))
        with open("../data/yml/gintama.yml", "a") as f2:
            
            if back:
                f2.write("  - " + line.split(",")[9])
                back = False
            if "？" in line.split(",")[9] and not back:
                f2.write("- - " + line.split(",")[9])
                back = True
