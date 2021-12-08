from dotenv import dotenv_values
from telegram.ext import Updater,CommandHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton


INPUT_TEXT  = 0  

config = dotenv_values(".env") 

def start(update, context):
    button1 = InlineKeyboardButton (
        text='Sobre el autor',
        url='https://github.com/nmorono'
    )
    button2 = InlineKeyboardButton (
        text='twitter',
        url='https://twitter.com'
    )
    update.message.reply_text(
        text='Haz click en un boton',
        reply_markup=InlineKeyboardMarkup([
            [button1], 
            [button2]
        ])
        )
 
if __name__ == '__main__':
    updater=Updater(token=config['MY_TOKEN'], use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start))

    updater.start_polling()
    updater.idle() 
