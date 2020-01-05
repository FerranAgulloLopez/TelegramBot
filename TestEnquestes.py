import sys
from antlr4 import *
from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from antlr4.InputStream import InputStream

input_stream = InputStream(open('TestInput.txt').read().strip())
lexer = EnquestesLexer(input_stream)
token_stream = CommonTokenStream(lexer)
print(token_stream.getText())
parser = EnquestesParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))
