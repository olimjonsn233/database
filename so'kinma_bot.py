from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
from telegram import ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton,KeyboardButton
import create_database
def start(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    name=update.message.chat.first_name
    create_database.saveuser(chat_id)
    
    bot.sendMessage(chat_id,f'''Salom{name} men so'kinganlarni xabarini o'chiraman
meni guruhga admin qiling''')

def sirlikalit(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt=update.message.text
    create_database.word(txt)
    
    bot.sendMessage(chat_id,"so'z muvafaqiyatli qo'shildi ortga qaytishingiz mumkin!")



updater = Updater('1365530589:AAEM6KjlnTiWCdaLqtKgDaw3Uc8gv9ZxTws')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('sirlikalit',sirlikalit))



updater.start_polling()
updater.idle()