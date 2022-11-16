from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from bot.bot_work.start_command import start, text_message
from django_project_finance.settings import TOKEN_TELEGRAM_BOT_API

def run_bot():

    """Основа бота: прокинули токен, подкючили команду старт, создали пулинг"""

    updater = Updater(TOKEN_TELEGRAM_BOT_API)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, callback=text_message))

    updater.start_polling()
    updater.idle()