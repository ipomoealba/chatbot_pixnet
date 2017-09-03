# -*- coding: utf-8 -*-
from chatterbot import ChatBot

import logging
logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    "Terminal",
    #  storage_adapter="chatterbot.storage.SQLStorageAdapter",
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    logic_adapters=[
        #  "chatterbot.logic.MathematicalEvaluation",
        #  "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="chatbot",
    database_uri="mongodb://iotbigdata:ipomoealbagmailcom@140.119.19.220:27017/",
    )

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
