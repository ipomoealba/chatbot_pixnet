#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
file_path = "/Users/chenhuawei/Dropbox/Code/Projects/chatbox/data/raw_data/WhyHim"
with open(file_path, "r") as f:
    back = 0
    for line in f.readlines():
        line = line.replace("\n", "")
        if re.match(r"(?!\d)\w",line[:3]) != None:    
            with open(file_path + ".yml", "a+") as f2:
                if back > 1:
                    back = 0

                if "？" in line:
                    f2.write(line + "\n")
                    back = 1
                elif back != 0:
                    f2.write(line + "\n")
                    back += 1

