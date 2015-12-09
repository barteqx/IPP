import  pickle
from twisted.internet import reactor
from udp_datagram_protocol import *
from tcp_factory import *
__author__ = 'Pawel'
"""
An example client. Run simpleserv.py first before running this.
"""


from multiprocessing import Process

# a client protocol
class Client(Process):
    def __init__(self, msg_callback, host, port):
        Process.__init__(self)
        self.msg_callback = msg_callback
        self.host = host
        self.udp_datagram_protocol = UdpDatagramProtocol(lambda msg: self.udp_data_received(msg), host)
        self.tcp_factory = TcpFactory(lambda msg: self.tcp_data_received(msg))
        self.port = port
        self.is_connected = False
        self.is_listening_on_udp = False
    def udp_data_received(self, msg):
        decoded_msg = pickle.dumps(msg)
        self.msg_callback(decoded_msg)

    def tcp_data_received(self, msg):
        decoded_msg = pickle.dumps(msg)
        self.msg_callback(decoded_msg)

    def listen_on_udp(self):
        reactor.listenUDP(0, self.udp_datagram_protocol)
        self.is_listening_on_udp = True

    def tcp_send_data(self, data):
        encoded_msg = pickle.loads(data)
        try:
            TcpFactory.sendData(encoded_msg)
        except ClientProtocolNotInitializedException:
            print "Client protocol not initialized - cannot send"

    def run(self):
        reactor.connectTCP(self.host, self.port, self.tcp_factory)
        reactor.run()
        self.is_connected = True