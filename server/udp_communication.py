__author__ = 'bartoszzasieczny'

from twisted.internet.protocol import DatagramProtocol


class UDPCommunication(DatagramProtocol):
    def sendData(self, datagram, address, port):
        self.transport.write(datagram, (address, port))