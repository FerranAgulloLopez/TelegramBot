import matplotlib.pyplot as plt
from functools import reduce
from datetime import datetime
from os.path import abspath

class Painter:

    def drawPie(self, report):
        labels = list(report.keys())
        values = list(report.values())
        sum = reduce(lambda count, x: count+x, values)
        sizes = [(x/sum)*100 for x in values]

        x = [i for i in range(len(labels))]
        fig, ax = plt.subplots()
        ax.set_title('Scores by option')
        ax.set_ylabel('Number of times selected')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        patches = ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)[0]
        plt.legend(patches, labels, loc="best")
        ax.axis('equal')

        path = 'data/auxiliary/' + str(datetime.now()).replace(' ', 'T') + '.png'
        plt.savefig(path)
        return abspath(path)

    def drawBar(self, report):
        labels = list(report.keys())
        values = list(report.values())

        x = [i for i in range(len(labels))]
        fig, ax = plt.subplots()
        ax.set_title('Scores by option')
        ax.set_ylabel('Number of times selected')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        plt.bar(x, values)
        fig.tight_layout()

        path = 'data/auxiliary/' + str(datetime.now()).replace(' ', 'T') + '.png'
        plt.savefig(path)
        return abspath(path)
