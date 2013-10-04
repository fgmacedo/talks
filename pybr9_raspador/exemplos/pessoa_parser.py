#coding: utf-8
from raspador import Parser
from raspador import StringField, IntegerField


class ParserDeInformacoesPessoais(Parser):
    Nome = StringField(r'Nome: (.*)')
    Idade = IntegerField(r'(\d+) anos')
