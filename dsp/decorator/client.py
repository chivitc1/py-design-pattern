import socket


def main():
    port = 2402
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    client.connect(('localhost', port))
    print("Received: {0}".format(client.recv(1024)))
    client.close()


if __name__ == '__main__':
    main()