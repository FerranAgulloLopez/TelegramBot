from antlr4 import *
from cl.EnquestesLexer import EnquestesLexer
from cl.EnquestesParser import EnquestesParser
from antlr4.InputStream import InputStream
from cl.EnquestesVisitor import EnquestesVisitor
import networkx as nx
import matplotlib.pyplot as plt
import pickle
import sys


def LexerPlusTokenizer(inputStream):
    lexer = EnquestesLexer(inputStream)
    return CommonTokenStream(lexer)


def Parser(tokenStream):
    parser = EnquestesParser(tokenStream)
    return parser.root()


def crearGraf(nodes, arestes):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(arestes)
    nx.draw_networkx(G, pos=nx.circular_layout(G), node_color='blue', edge_color='black')

    # dibuixar arestes amb etiquetes
    etiquetesItems = {}
    etiquetesAlternatives = {}
    for aresta in arestes:
        if len(aresta) > 2:
            data = aresta[-1]
            tipus = data['tipus']
            if tipus == 'item':
                etiquetesItems[(aresta[0], aresta[1])] = data['identificador']
            elif tipus == 'alternativa':
                etiquetesAlternatives[(aresta[0], aresta[1])] = data['identificador']
    nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels=etiquetesItems, font_color='red')
    nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels=etiquetesAlternatives, font_color='green')
    nom = [nbr for nbr in G.nodes() if G.nodes[nbr]['tipus'] == 'enquesta'][0]
    plt.savefig('data/quizs/' + nom + '.png')

    return nom, G


def pickleDump(graf, filename):
    outfile = open('data/quizs/' + filename + '.data', 'wb')
    pickle.dump(graf, outfile)
    outfile.close()


def main():
    nom = sys.argv[1]
    print("Llegint el fitxer " + nom)
    inputStream = InputStream(open('cl/input/' + nom).read().strip())
    tokenStream = LexerPlusTokenizer(inputStream)
    tree = Parser(tokenStream)
    visitor = EnquestesVisitor()
    nodes, arestes = visitor.visit(tree)
    nom, graf = crearGraf(nodes, arestes)
    pickleDump(graf, nom)


main()
