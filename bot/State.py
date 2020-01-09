from bot.DataManager import DataManager
from bot.Painter import Painter

class State:

    def __init__(self):
        # estats:
        # 0 -> Inicial
        # 1 -> Enquesta seleccionada
        # 2 -> Realitzant enquesta
        self.estat_actual = 0
        self.g = None # enquesta seleccionada
        self.nom_g = None
        self.pregunta_actual = None
        self.opcions_actuals = None
        self.report = None
        self.data = DataManager()
        self.painter = Painter()

    def seleccionarEnquesta(self, nom):
        text = []
        enquestesDisponibles = self.data.enquestesDisponibles()
        if self.estat_actual == 2:
            text.append('Invalidant enquesta començada')
        if nom in enquestesDisponibles:
            self.g = self.data.llegirEnquesta(nom)
            self.nom_g = nom
            self.estat_actual = 1
            text.append('Has seleccionat l\'enquesta ' + nom)
        else:
            self.estat_actual = 0
            text.append('L\'enquesta seleccionada no existeix')
        return text

    def isEnquestaSeleccionada(self):
        return self.estat_actual != 0

    def nomEnquestaSeleccionada(self):
        return self.nom_g

    def comencarEnquesta(self):
        if self.estat_actual == 0:
            return ['No hi ha cap enquesta seleccionada']
        else:
            text = []
            if self.estat_actual == 2:
                text.append('Invalidant enquesta començada')
            else:
                self.estat_actual = 2
            self.pregunta_actual = list(self.g.neighbors(self.nom_g))[0]
            self.report = {}
            text.append(self.textPregunta(self.pregunta_actual))
            return text

    def entradaText(self, entrada):
        text = []
        if self.estat_actual == 2:
            if entrada not in self.opcions_actuals:
                text.append('L\'opció seleccionada no és una de les mencionades. Si us plau indiqueu una de les opcions següents: ' + str(self.opcions_actuals))
            else:
                self.report[self.pregunta_actual] = {entrada: 1}
                text.append('Has seleccionat l\'opció ' + entrada)
                veins = self.g[self.pregunta_actual]
                alternatives = {}
                seguent = None
                for node in veins:
                    aresta = self.g[self.pregunta_actual][node]
                    tipus = aresta['tipus']
                    if tipus == 'seguent':
                        seguent = node
                    elif tipus == 'alternativa':
                        alternatives[aresta['identificador']] = node
                if entrada in alternatives:
                    self.pregunta_actual = alternatives[entrada]
                    text.append(self.textPregunta(self.pregunta_actual))
                else:
                    if seguent != None:
                        self.pregunta_actual = seguent
                        text.append(self.textPregunta(self.pregunta_actual))
                    else:
                        text.append('Enquesta finalitzada. Moltíssimes gràcies!')
                        self.estat_actual = 1
                        self.data.guardarReport(self.nom_g, self.report)
        return text


    def textPregunta(self, pregunta):
        text = pregunta + '> ' + self.g.nodes[pregunta]['text'] + '? \n'
        resposta = [nbr for nbr in self.g.neighbors(pregunta) if self.g.nodes[nbr]['tipus'] == 'resposta'][0]
        opcions = []
        for opcio in self.g.adj[resposta]:
            node = self.g.nodes.data()[opcio]
            text += node['identificadorOpcioResposta'] + ': ' + node['text'] + '\n'
            opcions.append(node['identificadorOpcioResposta'])
        self.opcions_actuals = opcions
        return text

    def drawPregunta(self, pregunta, tipus):
        if self.estat_actual == 0:
            return False, 'No hi ha cap enquesta seleccionada'
        elif pregunta not in self.g.nodes or self.g.nodes[pregunta]['tipus'] != 'pregunta':
            return False, 'La pregunta no existeix a l\'enquesta seleccionada'
        elif self.nom_g not in self.data.reportsDisponibles():
            return False, 'Encara no s\'ha contestat l\'enquesta cap vegada'
        else:
            report = self.data.llegirReport(self.nom_g)
            if pregunta not in report:
                return False, 'Encara no s\'ha contestat cap vegada aquesta pregunta'
            else:
                resposta = [nbr for nbr in self.g.neighbors(pregunta) if self.g.nodes[nbr]['tipus'] == 'resposta'][0]
                opcions = [self.g.nodes.data()[nbr]['identificadorOpcioResposta'] for nbr in self.g.adj[resposta]]
                for aux in opcions:
                    if aux not in report[pregunta]:
                        report[pregunta][aux] = 0
                if tipus == 'pie':
                    path = self.painter.drawPie(self.sortDict(report[pregunta]))
                else:
                    path = self.painter.drawBar(self.sortDict(report[pregunta]))
                return True, path

    def sortDict(self, dict):
        result = {}
        for aux in sorted(dict.keys()):
            result[aux] = dict[aux]
        return result

    def doReport(self):
        text = []
        if self.estat_actual == 0:
            text.append('No hi ha cap enquesta seleccionada')
        elif self.nom_g not in self.data.reportsDisponibles():
            text.append('Encara no s\'ha contestat l\'enquesta cap vegada')
        else:
            message = '*pregunta* *valor* *respostes* \n'
            report = self.data.llegirReport(self.nom_g)
            for pregunta in sorted(report.keys()):
                for resposta in sorted(report[pregunta].keys()):
                    message += pregunta + ' ' + resposta + ' ' + str(report[pregunta][resposta]) + '\n'
            text.append(message)
        return text






