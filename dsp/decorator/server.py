import socket

from logsocket import LogSocket
from gzipsocket import GzipSocket
from fictionconfig import config


def respond(client):
    response = input("Enter a value:")
    client.send(bytes(response, 'utf8'))
    client.close()


def main():
    port = 2402
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(1)
    print('server started on port', port)
    print('config: ', config)
    try:
        while True:
            # When a client connects
            client, addr = server.accept()

            # Requests data interactively and responds appropriately
            # respond(client)
            # respond(LogSocket(client))

            if config.get('log_send'):
                client = LogSocket(client)
            if client.getpeername()[0] in config.get('compress_hosts'):
                client = GzipSocket(client)
            respond(client)
    finally:
        server.close()


if __name__ == '__main__':
    main()