from telegram import ParseMode
from telegram.ext import CommandHandler
from bot.State import State
from bot.DataManager import DataManager
import json


class Handlers:

    def __init__(self):
        with open('bot/CommandsText.json') as file:
            self.text = json.load(file)
        self.state = State()
        self.dataReader = DataManager()

    def sendMessage(self, update, context, message):
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.MARKDOWN)

    def getHandlers(self):
        handlers = []
        handlers.append(CommandHandler('start', self.start))
        handlers.append(CommandHandler('author', self.author))
        handlers.append(CommandHandler('help', self.help))
        handlers.append(CommandHandler('show', self.show))
        handlers.append(CommandHandler('select', self.select))
        handlers.append(CommandHandler('diagram', self.diagram))
        # echo_handler = MessageHandler(Filters.text, echo)
        # dispatcher.add_handler(echo_handler)
        return handlers

    def start(self, update, context):
        self.sendMessage(update, context, self.text['start'])

    def author(self, update, context):
        self.sendMessage(update, context, self.text['author'])

    def help(self, update, context):
        self.sendMessage(update, context, self.text['help'])

    def show(self, update, context):
        enquestes = self.dataReader.enquestesDisponibles()
        text = self.text['show']
        for enquesta in enquestes:
            text += '\n - *' + enquesta + '*'
        self.sendMessage(update, context, text)

    def select(self, update, context):
        nom = update.message.text[8:]
        self.sendMessage(update, context, self.state.seleccionarEnquesta(nom))

    def diagram(self, update, context):
        if self.state.enquesta_seleccionada:
            path = self.dataReader.pathDiagrama(self.state.nom_enquesta_seleccionada)
            context.bot.send_photo(chat_id=update.message.chat_id, photo=open(path, 'rb'))
        else:
            self.sendMessage(update, context, 'No hi ha una enquesta seleccionada')