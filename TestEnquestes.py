import sys
from antlr4 import *
from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from antlr4.InputStream import InputStream
from EnquestesVisitor import EnquestesVisitor
import networkx as nx
import matplotlib.pyplot as plt

input_stream = InputStream(open('TestInput.txt').read().strip())
lexer = EnquestesLexer(input_stream)
token_stream = CommonTokenStream(lexer)
#print(token_stream.getText())
parser = EnquestesParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))
print()
print()
visitor = EnquestesVisitor()
print(visitor)
nodes, edges = visitor.visit(tree)
print()
print()
print(nodes)
print(edges)
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)



nx.draw_networkx(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
plt.savefig('meh.png')

#COMPROBAR CICLOS COÑO
