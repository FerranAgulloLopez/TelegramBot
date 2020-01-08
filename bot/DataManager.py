from os import listdir
from os.path import abspath
from os.path import isfile, join
import pickle
import re

class DataManager:

    def __init__(self):
        self.pathEnquesta = 'data/quizs/'
        self.pathReport = 'data/reports/'

    def enquestesDisponibles(self):
        return {re.sub(r'.data|.png', '', f) for f in listdir(self.pathEnquesta) if isfile(join(self.pathEnquesta, f))}

    def llegirEnquesta(self, nom):
        path = self.pathEnquesta + nom + '.data'
        infile = open(path, 'rb')
        data = pickle.load(infile)
        infile.close()
        return data

    def pathDiagrama(self, nom):
        path = self.pathEnquesta + nom + '.png'
        return abspath(path)

    def llegirReport(self, nom):
        path = self.pathReport + nom + '.data'
        infile = open(path, 'rb')
        data = pickle.load(infile)
        infile.close()
        return data

    def guardarReport(self, nomEnquesta, report):
        reports = {f.replace('.data', '') for f in listdir(self.pathReport) if isfile(join(self.pathReport, f))}
        if nomEnquesta in reports:
            aux = self.llegirReport(nomEnquesta)
            report = self.mergeReports(aux, report)
        outfile = open(self.pathReport + nomEnquesta + '.data', 'wb')
        pickle.dump(report, outfile)
        outfile.close()

    def mergeReports(self, report, report2):
        for pregunta in report2:
            if pregunta in report:
                for opcio in report2[pregunta]:
                    if opcio in report[pregunta]:
                        report[pregunta][opcio] += report2[pregunta][opcio]
                    else:
                        report[pregunta][opcio] = report2[pregunta][opcio]
            else:
                report[pregunta] = report2[pregunta]
        return report
