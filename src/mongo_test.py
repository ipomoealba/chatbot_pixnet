#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo 
from pymongo import MongoClient
uri = "mongodb://iotbigdata:ipomoealbagmailcom@140.119.19.220:27017"

client = MongoClient(uri)
db = client["admin"]
db.findAll()
