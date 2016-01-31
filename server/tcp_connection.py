__author__ = 'Pawel'

from twisted.internet import protocol
from twisted.internet.protocol import DatagramProtocol


class TCPConnection(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    def __init__(self, msg_callback, addr):
        self.publish = msg_callback
        self.addr = addr

    def dataReceived(self, data):
        self.publish(data, self.addr)

    def sendData(self, data):
        self.transport.write(data)

    def connectionLost(self, reason):
        self.publish(-1, self.addr)


class TCPFactory(protocol.ServerFactory):
    def __init__(self, msg_callback):
        self.publish = msg_callback
        self.clients = {}

    def buildProtocol(self, addr):
        client = TCPConnection(self.publish, addr)
        self.clients[addr.host] = client
        return client
