__author__ = 'bartoszzasieczny'
import pickle
from twisted.internet import reactor

from server_events import *
from tcp_connection import *
from udp_communication import *
from core.communication_model import *

class MappingEntry:
    def __init__(self, obj):
        self.addr = obj.addr
        self.port = obj.port
        self.id = obj.id

class Connection(object):

    def __init__(self, config, event_aggregator):
        self.config = config
        self.event_aggregator = event_aggregator
        self.factory = TCPFactory(self.publish)
        self.subscribe_to_events()
        self.UDP = UDPCommunication()
        self.mapping = {}

    def notify(self, event):

        if event.type == ServerEventTypes.UPDATE:
            print "Sending physics update..."
            physics_update = PhysicsUpdate(event.args["objects"], event.args["ids_to_delete"])
            self.pickle_and_send_to_all(physics_update, True)

        if event.type == ServerEventTypes.HANDSHAKERESPONSE:
            handshake_response = HandshakeResponse(event.args["object"], event.args["ok"])
            pickled = pickle.dumps(handshake_response)
            self.mapping[event.args["addr"]] = MappingEntry(event.args["object"])
            self.factory.clients[event.args["object"].addr].tcp_send_data(pickled)

    def set_up_connection(self):
        print "Setting up connection..."
        self.factory.protocol = TCPConnection
        reactor.listenTCP(self.config.port_TCP, self.factory)

        reactor.run()

    def publish(self, message, addr):
        msg = pickle.loads(message)

        if type(msg) == PlayerMovement:
            args = {
                "id": self.mapping[addr].id,
                "movement": msg
            }
            self.event_aggregator.publish(PlayerMovementEvent(args))


        if type(msg) == PlayerDescription:
            args = {
                "name": msg.name,
                "udp_port": msg.udp_port,
                "addr": addr.host
            }
            self.event_aggregator.publish(HandshakeEvent(args))

        if type(msg) == PlayerQuit:
            args = {
                "id": self.mapping[addr].id
            }
            self.event_aggregator.publish(QuitEvent(args))
            self.factory.clients[addr].loseConnection()
            del self.factory.clients[addr]

    def pickle_and_send_to_all(self, message, udp=False):
        pickled = pickle.dumps(message)
        for k, v in self.factory.clients.items():
            if not udp:
                v.tcp_send_data(pickled)

            else:
                self.UDP.sendData(k, self.mapping[k].port)

    def subscribe_to_events(self):
        self.event_aggregator.subscribe(self, ServerEventTypes.UPDATE)
        self.event_aggregator.subscribe(self, ServerEventTypes.OBJECTDESTRUCTION)
        self.event_aggregator.subscribe(self, ServerEventTypes.OBJECTCREATION)
        self.event_aggregator.subscribe(self, ServerEventTypes.HANDSHAKERESPONSE)


def connection_init(event_aggregator, config):

    connection_process = Connection(config, event_aggregator)

    # subscribe for events

    return connection_process