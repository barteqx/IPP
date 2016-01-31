__author__ = 'bartoszzasieczny'

from twisted.internet.protocol import DatagramProtocol

class UDPCommunication(DatagramProtocol):
    def sendData(self, datagram, address, port):
        print datagram
        self.transport.write(datagram, (address, port))