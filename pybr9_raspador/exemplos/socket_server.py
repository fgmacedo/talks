import socket


def ler_socket(port):
    HOST = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, port))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
        data = conn.recv(1024)
        if not data or data.strip() == 'sair':
            break
        yield data
    conn.close()
