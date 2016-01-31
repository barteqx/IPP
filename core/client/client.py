import  pickle
from twisted.internet import reactor
from udp_datagram_protocol import *
from tcp_factory import *
__author__ = 'Pawel'
"""
An example client. Run simpleserv.py first before running this.
"""


from multiprocessing import Process
from core.communication_model import PlayerDescription
import threading
import copy

# a client protocol
class Client(threading.Thread):
    def __init__(self, msg_callback, host, port, name="pawel", udp_port=8001):
        threading.Thread.__init__(self)
        print(udp_port)
        print(host)
        self.msg_callback = msg_callback
        self.host = host
        self.name = name
        self.udp_port = udp_port

        self.handshake_message = pickle.dumps(PlayerDescription(self.name, self.udp_port))
        self.udp_datagram_protocol = UdpDatagramProtocol(self.udp_data_received, self.host)
        self.tcp_factory = TcpFactory(self.tcp_data_received, self.handshake_message)
        self.port = port
        self.is_connected = False
        self.is_listening_on_udp = False
        self.event_queue = []

    def udp_data_received(self, msg):
        decoded_msg = pickle.loads(msg)
        print("udp client")
        self.event_queue.append(decoded_msg)

    def tcp_data_received(self, msg):
        decoded_msg = pickle.loads(msg)
        print("tcp data received")
        self.msg_callback(decoded_msg)

    def listen_on_udp(self):
        reactor.listenUDP(self.udp_port, self.udp_datagram_protocol)
        self.is_listening_on_udp = True

    def tcp_send_data(self, data):
        encoded_msg = pickle.dumps(data)
        try:
            TcpFactory.sendData(encoded_msg)
        except ClientProtocolNotInitializedException:
            print "Client protocol not initialized - cannot send"

    def run(self):
        reactor.connectTCP(self.host, self.port, self.tcp_factory)
        self.listen_on_udp()
        reactor.run(installSignalHandlers=False)
        print("podlaczony")
        self.is_connected = True

    def handle_player_movement(self, player_movement):
        self.tcp_send_data(player_movement)

    def get_events(self):
        events = copy.copy(self.event_queue)
        self.event_queue = []
        return events
