__author__ = 'bartoszzasieczny'

from twisted.internet.protocol import DatagramProtocol


class UDPCommunication(DatagramProtocol):
    def datagramReceived(self, datagram, address):
        print datagram