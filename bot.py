import logging

import datetime

from base import MachineLearning
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from database import Database
Token = ""
updater = Updater(token=Token)
dispatcher = updater.dispatcher
logging.basicConfig(filename="sato.log",level=logging.INFO)
logger = logging.getLogger("Log")




ml = MachineLearning()
db = Database()
def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text="Sorunuzu yazın tatlım :)")

def question(bot, update):

    question = update.message.text
    real_question = ml.find(question)
    answer = db.ReturnAnswer(real_question)
    if(real_question!="None\n"):
        bot.sendMessage(chat_id = update.message.chat_id, text=real_question)
    bot.sendMessage(chat_id = update.message.chat_id, text=answer)
    log = {"username": update.message.from_user.username, "message": question , "datetime":datetime.datetime.now(),
           "first_name":update.message.from_user.first_name
           }
    logger.debug(log)
    logger.info(log)

start_handler = CommandHandler('start', start)
question_handler = MessageHandler(Filters.text, question)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(question_handler)



updater.start_polling()
