from antlr4 import *
from cl.EnquestesLexer import EnquestesLexer
from cl.EnquestesParser import EnquestesParser
from antlr4.InputStream import InputStream
from cl.EnquestesVisitor import EnquestesVisitor
import networkx as nx
import matplotlib.pyplot as plt
import pickle

def LexerPlusTokenizer(inputStream):
    lexer = EnquestesLexer(inputStream)
    return CommonTokenStream(lexer)
    
def Parser(tokenStream):
    parser = EnquestesParser(tokenStream)
    #tree = parser.root()
    #print(tree.toStringTree(recog=parser))
    return parser.root()

def crearGraf(nodes, arestes):
    # buscar el nom de l'enquesta
    nom = None
    for node in nodes:
        if len(node) > 1:
            data = node[-1]
            tipus = data['tipus']
            if tipus == 'enquesta':
                nom = data['identificador']
                break

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
    plt.savefig('data/'+nom+'.png')

    print(G.nodes.data()['E'])
    print(list(G.neighbors('E')))
    print(G.nodes['P1'])
    return nom, G


def pickleDump(graf,filename):
    outfile = open('data/'+filename+'.data', 'wb')
    pickle.dump(graf, outfile)
    outfile.close()

def main():
    inputStream = InputStream(open('cl/TestInput.txt').read().strip())
    tokenStream = LexerPlusTokenizer(inputStream)
    tree = Parser(tokenStream)
    visitor = EnquestesVisitor()
    nodes, arestes = visitor.visit(tree)
    nom, graf = crearGraf(nodes,arestes)
    pickleDump(graf, nom)

main()
