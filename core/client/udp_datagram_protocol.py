from twisted.internet.protocol import DatagramProtocol

__author__ = 'Pawel'


class UdpDatagramProtocol(DatagramProtocol):
    def __init__(self, msg_callback, host):
        self.msg_callback = msg_callback
        self.host = host

    def datagramReceived(self, datagram, host):
        if self.host is not host:
            return
        self.msg_callback(datagram)
