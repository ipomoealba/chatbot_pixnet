#!/usr/bin/env python
# -*- coding: utf-8 -*-
data = ""
with open("../yml/qa.yml", 'r') as f:
    for line in f:
        try:
            if line.index(".") < 4:
                line = "- - " + line[line.index(".")+1:]    
                data += line 
            elif line =="\n":
                pass
        except Exception: 
            if line != "\n":
                data += line 
with open("../yml/qa1.yml", 'w+') as f:
    f.write(data)

