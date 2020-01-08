from bot.DataManager import DataManager


class State:

    def __init__(self):
        # estats:
        # 0 -> Inicial
        # 1 -> Enquesta seleccionada
        # 2 -> Realitzant enquesta
        self.estat_actual = 0
        self.enquesta_seleccionada = None
        self.nom_enquesta_seleccionada = None
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
