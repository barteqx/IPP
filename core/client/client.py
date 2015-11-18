__author__ = 'Pawel'
"""
An example client. Run simpleserv.py first before running this.
"""

from twisted.internet import reactor, protocol
from twisted.internet.protocol import DatagramProtocol


# a client protocol

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""

    def connectionMade(self):
        self.transport.write("hello, world!")

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print " TCP Server said:", data
        self.transport.loseConnection()

    def connectionLost(self, reason):
        print "connection lost"

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"

    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"

class UdpClient(DatagramProtocol):
    """Once connected, send a message, then print the result."""

    def __init__(self, reactor):
        self._reactor = reactor

    def startProtocol(self):
        self.transport.connect("192.168.0.7", 8008)
        self.transport.write("1488")
        print "poszlo!"

    def datagramReceived(self, data, host):
        "As soon as any data is received, write it back."
        print "UDP Server said:", repr(data)
        self._reactor.stop()




# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()
    reactor.connectTCP("192.168.0.7", 8009, f)
    reactor.listenUDP(8008, UdpClient(reactor))
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
