from bot.DataManager import DataManager
import networkx as nx

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

