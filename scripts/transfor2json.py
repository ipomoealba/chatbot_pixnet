#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

datasets = ["fanzxl", "fk24", "housys"]


def transfor2json(dataset):
    data = []
    tmp = ""
    with open("../data/raw_data_from_series/" + dataset + ".txt", 'r') as f:
        for line in f:
            line = line.replace("\'", "").replace("\"", "")
            #  print(line)
            if line[0] == 'E':
                print("Close a conversation")
                tmp = ""
            elif line[0] == 'M':
                if tmp != "":
                    data.append([tmp[2:], line[2:]])
                    #  print([tmp, line])
                else:
                    pass
                tmp = line
            else:
                pass

    with open(dataset + '.json', 'w') as outfile:
        json.dump({dataset: data}, outfile)


map(transfor2json, datasets)
