#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import logging
import csv
import jieba
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

logging.basicConfig(level=logging.DEBUG)

#  jieba.load_userdict("../jieba_dict/av.txt")
#  jieba.load_userdict("../jieba_dict/dict.txt")
#  jieba.load_userdict("../jieba_dict/ptt_words.txt")
#  jieba.load_userdict("../jieba_dict/taiwan_actor.txt")
#  jieba.load_userdict("../jieba_dict/taiwan_name.txt")
#  jieba.load_userdict("../jieba_dict/usa_name.txt")
stopwords = []
can_words = []

with open("../data/stopwords/stopwords", 'r') as f:
    stopwords = [i.replace(" ", "") for i in f.read().split("\n")]
with open("../data/cans/cans.txt", "r") as f:
    can_words = f.read().split("\n")
__bot = ChatBot(
    "I wonna sleep....",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.BestMatch",
        #  {
        #  'import_path': 'chatterbot.logic.LowConfidenceAdapter',
        #  'threshold': 0.5,
        #  'default_response': '我是不知道你在供三小啦 但我不想人生攻擊你'
        #  }
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    language="chinese",
)


print("Type something to begin...")


def remove_stopwords(words):
    for i in stopwords:
        if i in words:
            words.remove(i)
    return words


while True:
    try:
        __input = input()
        with open("../data/keywords.csv", 'r') as f:
            reader = csv.DictReader(f)
            dont_use_chatter = False
            for row in reader:
                if row["QUESTION"] in __input:
                    logging.debug("the words in my db")
                    print(row["ANSWER"])
                    dont_use_chatter = True
                    break
            if dont_use_chatter == False:
                bot_input = __bot.get_response(__input)
                logging.debug("confidence" + str(bot_input.confidence))
                if bot_input.confidence > 0.5:
                    print(bot_input)
                    dont_use_chatter = True
                else:
                    logging.debug("confidence too low, try to search")
                    segs = jieba.cut(__input)
                    dont_use_chatter = True
                    segged = list(segs)
                    without_sw = remove_stopwords(segged)
                    logging.debug("without stopword: " + "".join(without_sw))
                    new_bot_input = random.choice(can_words).replace("%p", __input)
                    print(new_bot_input)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
