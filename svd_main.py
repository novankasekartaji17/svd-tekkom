import svd_lexer
import svd_parser
import svd_interp

from sys import *

#DENGAN MASUKAN EKSTENSI .SVD
lexer = svd_lexer.BasicLexer()
parser = svd_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    svd_interp.BasicExecute(tree, env)
