__author__ = 'Pawel'

from twisted.internet import reactor, protocol
from twisted.internet.protocol import DatagramProtocol


class EchoUDP(DatagramProtocol):
    def datagramReceived(self, datagram, address):
        print(datagram)
        self.transport.write(datagram, address)

class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        self.transport.write(data)
        print("dataReceived")


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8009,factory)

    #reactor.run()

    reactor.listenUDP(8008, EchoUDP())
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
