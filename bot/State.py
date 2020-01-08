from bot.DataManager import DataManager
import networkx as nx

class State:

    def __init__(self):
        # estats:
        # 0 -> Inicial
        # 1 -> Enquesta seleccionada
        # 2 -> Realitzant enquesta
        self.estat_actual = 0
        self.enquesta_seleccionada = None
        self.nom_enquesta_seleccionada = None
        self.pregunta_actual = None
        self.data = DataManager()

    def seleccionarEnquesta(self, nom):
        enquestesDisponibles = self.data.enquestesDisponibles()
        if nom in enquestesDisponibles:
            self.enquesta_seleccionada = self.data.llegirEnquesta(nom)
            self.nom_enquesta_seleccionada = nom
            self.estat_actual = 1
            return 'Has seleccionat l\'enquesta ' + nom
        else:
            self.estat_actual = 0
            return 'L\'enquesta seleccionada no existeix'

    def isEnquestaSeleccionada(self):
        return self.estat_actual != 0

    def nomEnquestaSeleccionada(self):
        return self.nom_enquesta_seleccionada

    def comencarEnquesta(self):
        if self.estat_actual == 0:
            return ['No hi ha cap enquesta seleccionada']
        else:
            text = []
            if self.estat_actual == 2:
                text.append('Invalidant enquesta començada.')
            self.pregunta_actual = list(self.enquesta_seleccionada.neighbors(self.nom_enquesta_seleccionada))[0]
            text.append(self.textPregunta(self.pregunta_actual))
            return text

    def textPregunta(self, pregunta):
        text = self.enquesta_seleccionada.nodes[pregunta]['text']
        return pregunta + '> ' + text + '?'

