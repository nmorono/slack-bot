import qrcode
import os
from dotenv import dotenv_values
from telegram.ext import Updater,CommandHandler,ConversationHandler,MessageHandler,Filters
from telegram import ChatAction

INPUT_TEXT  = 0  

config = dotenv_values(".env") 


def start(update, context):
    update.message.reply_text('Hola, bienvenido, que deseas hacer?\n\nUsa /qr para generar un codigo qr')

def qr_command_handler(update, context):
    update.message.reply_text('Envíame un texto para generarte un código qr por favor.')
    return INPUT_TEXT

def generate_qr(text):
    filename = text + '.jpg'
    img = qrcode.make(text)
    img.save(filename)
    return filename

def send_qr(filename,chat):
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO, 
        timeout=None 
    )
    chat.send_photo(
        photo=open(filename,'rb')
    )
    os.unlink(filename)

def input_text(update, context): 
    text = update.message.text
    filename = generate_qr(text)
    chat = update.message.chat
    send_qr(filename, chat) 
    return ConversationHandler.END
 
if __name__ == '__main__':
    updater=Updater(token=config['MY_TOKEN'], use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr',qr_command_handler)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)] 
        },
        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle() 
   