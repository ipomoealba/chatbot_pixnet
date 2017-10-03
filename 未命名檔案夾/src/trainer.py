#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import csv
import jieba
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
logging.basicConfig(level=logging.INFO)


def raw_data_transfer(file_path):
    with open("../data/keywords.csv", "r") as f:
        for i in csv.DictReader(f):
            with open("../data/yml/keywords.yml", "a+") as f2:
                f2.write("- - " + i["QUESTION"] + "\n" +"  - " + i["ANSWER"] + "\n")


raw_data_transfer("../data/keywords.csv")
logging.info("data transfer to yml")
bot = ChatBot(
    "I wonna sleep....",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.BestMatch",
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.5,
            'default_response': '我是不知道你在供三小啦 但我不想人生攻擊你'
        }
        ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    language="chinese",
)
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train(
    "../data/yml/conversation.yml",
    #  "../data/yml/fk24.yml",
    #  "../data/yml/mingfb.yml",
    "../data/yml/keywords.yml",
    "../data/yml/dirty_grandpa_new.yml",
    "../data/yml/gintama.yml",
    )

print("training done")
