__author__ = 'Pawel'

from twisted.internet import protocol
from twisted.protocols.basic import NetstringReceiver
from twisted.internet.protocol import DatagramProtocol


class TCPConnection(NetstringReceiver):
    """This is just about the simplest possible protocol"""

    def __init__(self, msg_callback, addr):
        self.publish = msg_callback
        self.addr = addr

    def stringReceived(self, data):
        self.publish(data, self.addr)

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
