#coding: utf-8
from __future__ import print_function

from raspador import Parser
from raspador import StringField, IntegerField


class ParserDeInformacoesPessoais(Parser):
    Nome = StringField(r'Nome: (.*)')
    Idade = IntegerField(r'(\d+) anos')