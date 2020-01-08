from os import listdir
from os.path import abspath
from os.path import isfile, join
import pickle
import re

class DataManager:

    def __init__(self):
        self.path = 'data/'

    def enquestesDisponibles(self):
        return {re.sub(r'.data|.png', '', f) for f in listdir(self.path) if isfile(join(self.path, f))}

    def llegirEnquesta(self, nom):
        path = self.path + nom + '.data'
        infile = open(path, 'rb')
        data = pickle.load(infile)
        infile.close()
        return data

    def pathDiagrama(self, nom):
        path = self.path + nom + '.png'
        return abspath(path)
