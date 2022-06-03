from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import CallbackQuery
from telegram.ext import CallbackQueryHandler
TOKEN = '5330702496:AAHIsy8_N-_yjWTr-o4MhVqhryfpniVQJ5c'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_game(chat_id=update.effective_chat.id, game_short_name="AntonRush")

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
updater.start_polling()

def button(update, context):
    user = update.effective_user
    query: CallbackQuery = update.callback_query
    query.answer(url='http://3.145.21.24:8080/')

dispatcher.add_handler(CallbackQueryHandler(button))