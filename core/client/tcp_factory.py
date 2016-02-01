from twisted.internet import reactor, protocol
from twisted.protocols.basic import NetstringReceiver
__author__ = 'Pawel'

class TcpClient(NetstringReceiver):

    def __init__(self, msg_callback, handshake_message):
        self.msg_callback = msg_callback
        self.handshake_message = handshake_message

    def connectionMade(self):
        #print("connection made")
        self.sendString(self.handshake_message)

    def stringReceived(self, data):
        #print("data received")
        self.msg_callback(data)

    def connectionLost(self, reason):
        print "connection lost"


class TcpFactory(protocol.ClientFactory):

    client_protocol = None

    def __init__(self, msg_callback, handshake_message):
        self.msg_callback = msg_callback
        self.handshake_message = handshake_message

    def buildProtocol(self, addr):
        TcpFactory.client_protocol = TcpClient(self.msg_callback, self.handshake_message)
        return TcpFactory.client_protocol

    @staticmethod
    def sendData(data):
        if not TcpFactory.client_protocol:
            raise ClientProtocolNotInitializedException

        TcpFactory.client_protocol.sendString(data)

class ClientProtocolNotInitializedException(Exception):
    pass
