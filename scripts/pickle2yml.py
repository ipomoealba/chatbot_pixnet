#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
with open("/Users/chenhuawei/Dropbox/Code/Projects/chatbox/data/raw_data/ming.pkl", "rb") as f:
    with open("./mingfb.yml", "a+") as f2:
        while True:
            text = pickle.load(f)

            f2.write("- - "+ text['Q'].replace("\n", "") + "\n")
            f2.write("  - "+ text['A'].replace("\n", "") + "\n")
