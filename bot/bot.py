from telegram.ext import Updater
from bot.Handlers import Handlers
import logging

TOKEN = open('bot/token.txt').read().strip()


def main():
    handlers = Handlers().getHandlers()
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    for handler in handlers:
        dispatcher.add_handler(handler)
    updater.start_polling()


main()
