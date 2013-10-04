#coding: utf-8
import sys

from socket_server import ler_socket
from socket_parser import ParserDeMensagens

porta = int(sys.argv[1]) if len(sys.argv) > 1 else 5010

parser = ParserDeMensagens()

print "Ouvindo na porta {}".format(porta)
for item in parser.parse(ler_socket(porta)):
    print item

    if 'Pessoa' in item:
        print "Pessoa encontrada: {Nome}, tem {Idade}.".format(**item.Pessoa)

    if 'Erro' in item:
        print "***Erro {Codigo}: {Mensagem}.".format(**item.Erro)
