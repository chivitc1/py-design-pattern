class LogSocket:
    """This class decorates a socket object and presents the send and close interface to
    client sockets."""
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print('Sending {0} to {1}'.format(data, self.socket.getpeername()[0]))
        self.socket.send(data)

    def close(self):
        self.socket.close()

    def getpeername(self):
        return self.socket.getpeername()