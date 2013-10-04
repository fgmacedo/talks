#coding: utf-8

from raspador import Parser
from raspador import StringField, IntegerField


class ParserDeErro(Parser):
    begin = r'erro'
    end = r'fim'
    Mensagem = StringField(r'msg:\s*(.*)')
    Codigo = IntegerField(r'cod:\s*(\d+)')


class ParserDePessoa(Parser):
    begin = r'info'
    end = r'fim'
    Nome = StringField(r'(?i)Nome:\s*(.*)')
    Idade = IntegerField(r'(?i)Idade:\s*(\d+)')


class ParserDeMensagens(Parser):
    yield_item_to_each_field_value_found = True

    Erro = ParserDeErro()
    Pessoa = ParserDePessoa()
