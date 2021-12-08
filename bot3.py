import os
from telegram.ext import Updater,MessageHandler
from dotenv import dotenv_values

config = dotenv_values(".env") 

if __name__ == '__main__':
    updater=Updater(token=config['MY_TOKEN'], use_context=True)
    dp=updater.dispatcher


    updater.start_polling()
    print('Bot is polling')
    updater.idle() 
