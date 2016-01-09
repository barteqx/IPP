__author__ = 'bartoszzasieczny'

from twisted.internet.protocol import DatagramProtocol


class UDP(DatagramProtocol):
    def datagramReceived(self, datagram, address):
        print datagram