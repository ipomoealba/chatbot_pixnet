#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import re
datasets = ["fanzxl", "fk24", "housys"]


def transfor2json(dataset):
    data = """categories:
- chinese
- %s
conversations:
    """%(dataset)
    tmp2 = "- - "
    with open("../data/raw_data_from_series/" + dataset + ".txt", 'r') as f:
        tmp2 = "- - "
        tmp_conversation = ""
        lock = True
        for line in f:
            line = line.replace("\'", "").replace("\"", "").replace(":", "")
            #  print(line)
            if line.replace("\n", "") == "":
                pass
            else:
                if line[0] == 'E' and lock == True:
                    tmp2 = "- - " 
                    data += tmp_conversation
                    tmp_conversation = ""
                    lock = False
                    # data += "\n" + tmp2 + line[2:]
                elif line[0] == 'M' and lock==False:
                    if re.search('[a-zA-Z]', line[2:]):
                        lock = True 
                    else:
                        tmp_conversation += tmp2 + line[2:]      
                        tmp2 = "  - "
                else:
                    pass
    
    with open(dataset + '.yml', 'w') as outfile:
        outfile.write(data)


map(transfor2json, datasets)
