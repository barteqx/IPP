from twisted.internet import reactor, protocol
__author__ = 'Pawel'

class TcpClient(protocol.Protocol):

    def __init__(self, msg_callback):
        self.msg_callback = msg_callback

    def connectionMade(self):
        self.transport.write("Hi, my name is ... ")

    def dataReceived(self, data):
        self.msg_callback(data)

    def connectionLost(self, reason):
        print "connection lost"

    def sendData(self, data):
        self.transport.write(data)
class TcpFactory(protocol.ClientFactory):

    client_protocol = None

    def __init__(self, msg_callback):
        self.msg_callback = msg_callback

    def buildProtocol(self, addr):
        TcpFactory.client_protocol = TcpClient(self.msg_callback)
        return TcpFactory.client_protocol

    @staticmethod
    def sendData(data):
        if not TcpFactory.client_protocol:
            raise ClientProtocolNotInitializedException

        TcpFactory.client_protocol.sendData(data)

class ClientProtocolNotInitializedException(Exception):
    pass
