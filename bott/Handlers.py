from telegram import ParseMode
from telegram.ext import CommandHandler, MessageHandler, Filters
from bott.State import State
from bott.DataManager import DataManager
import json


class Handlers:

    def __init__(self):
        with open('bott/CommandsText.json') as file:
            self.text = json.load(file)
        self.state = State()
        self.dataReader = DataManager()

    def sendMessage(self, update, context, message):
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.MARKDOWN)

    def sendPhoto(self, update, context, path):
        context.bot.send_photo(chat_id=update.message.chat_id, photo=open(path, 'rb'))

    def getHandlers(self):
        handlers = []
        handlers.append(CommandHandler('start', self.start))
        handlers.append(CommandHandler('author', self.author))
        handlers.append(CommandHandler('help', self.help))
        handlers.append(CommandHandler('show', self.show))
        handlers.append(CommandHandler('select', self.select))
        handlers.append(CommandHandler('diagram', self.diagram))
        handlers.append(CommandHandler('quiz', self.quiz))
        handlers.append(CommandHandler('pie', self.pie))
        handlers.append(CommandHandler('bar', self.bar))
        handlers.append(CommandHandler('report', self.report))
        handlers.append(MessageHandler(Filters.text, self.input))
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
        if update.message is not None:
            nom = update.message.text[8:]
            text = self.state.seleccionarEnquesta(nom)
            for message in text:
                self.sendMessage(update, context, message)

    def diagram(self, update, context):
        if self.state.isEnquestaSeleccionada:
            path = self.dataReader.pathDiagrama(self.state.nom_g)
            self.sendPhoto(update, context, path)
        else:
            self.sendMessage(update, context, 'No hi ha cap enquesta seleccionada')

    def quiz(self, update, context):
        text = self.state.comencarEnquesta()
        for message in text:
            self.sendMessage(update, context, message)

    def input(self, update, context):
        if update.message is not None:
            entrada = update.message.text
            text = self.state.entradaText(entrada)
            for message in text:
                self.sendMessage(update, context, message)

    def pie(self, update, context):
        if update.message is not None:
            nom = update.message.text[5:]
            ok, text = self.state.drawPregunta(nom, 'pie')
            if ok:
                self.sendPhoto(update, context, text)
                self.dataReader.borrarAuxiliaryFile(text)
            else:
                self.sendMessage(update, context, text)

    def bar(self, update, context):
        if update.message is not None:
            nom = update.message.text[5:]
            ok, text = self.state.drawPregunta(nom, 'bar')
            if ok:
                self.sendPhoto(update, context, text)
                self.dataReader.borrarAuxiliaryFile(text)
            else:
                self.sendMessage(update, context, text)

    def report(self, update, context):
        text = self.state.doReport()
        for message in text:
            self.sendMessage(update, context, message)
