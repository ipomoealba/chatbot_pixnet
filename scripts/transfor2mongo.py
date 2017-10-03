#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import datetime
from pymongo.errors import DuplicateKeyError

from pymongo import MongoClient
uri = "mongodb://192.168.99.100"
client = MongoClient(uri)
datasets = ["fanzxl", "fk24", "housys"]

db = client['chatbot']
collect = db['statements']


def transfor2mongo(dataset):
    data = []
    tmp = ""
    with open("../data/raw_data_from_series/" + dataset + ".txt", 'r') as f:
        for line in f:
            line = line.replace("\'", "").replace("\"", "")
            print(line)
            if line[0] == 'E':
                tmp = ""
            elif line[0] == 'M':
                if tmp != "":
                    data.append([tmp[2:], line[2:]])
                    data_dict = {"text": tmp[2:].replace("\n", ""), "in_response_to": {"text": line[2:].replace(
                        "\n", ""), "created_at": datetime.datetime.utcnow()}, "created_at": datetime.datetime.utcnow()}
                    try:
                        post_id = collect.update(
                                {"text": tmp[2:]}, {'$set':  {
                                    "created_at": datetime.datetime.utcnow(),
                                    "extra_data":{},
                                    }
                                    ,'$push': {"in_response_to": {"text": line[2:].replace("\n", ""
                                        ), "created_at": datetime.datetime.utcnow()},
                                        "occurrence": 0
                                        }}, upsert=True)
                    except DuplicateKeyError:
                        pass
                #  print([tmp, line])

                    data_dict = {}
                else:
                    pass
                tmp = line
            else:
                pass


map(transfor2mongo, datasets)
