#coding: utf-8
from __future__ import print_function

from pessoa_parser import ParserDeInformacoesPessoais

parser = ParserDeInformacoesPessoais()

with open('pessoa.txt') as f:
    for pessoa in parser.parse(f):
        print(pessoa.Nome)
        print(pessoa.Idade)


# parser.parse retorna um generator
with open('pessoa.txt') as f:
    g = parser.parse(f)
    print(type(g))
    print(next(g))
