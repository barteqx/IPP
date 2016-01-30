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
            physics_update = PhysicsUpdate(event.args["objects"], event.args["to_delete"])
            self.pickle_and_send_to_all(physics_update, True)

        if event.type == ServerEventTypes.OBJECTCREATION:
            creation = ObjectCreation(event.args["object"], event.args["object_type"])
            self.mapping[event.args["addr"]] = MappingEntry(event.args["object"])
            self.pickle_and_send_to_all(creation)

        if event.type == ServerEventTypes.OBJECTDESTRUCTION:
            destruction = ObjectDestruction(event.args["object"].id)
            del self.mapping[event.args["object"].addr]
            self.pickle_and_send_to_all(destruction)

    def set_up_connection(self):
        self.factory.protocol = TCPConnection
        reactor.listen(self.config.port_TCP, self.factory)

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
                "addr": addr
            }
            self.event_aggregator.publish(HandshakeEvent(args))

        if type(msg) == PlayerQuit:
            args = {
                "id": self.mapping[addr].id
            }
            self.event_aggregator.publish(QuitEvent(args))

    def pickle_and_send_to_all(self, message, udp=False):
        pickled = pickle.dumps(message)
        for k, v in self.factory:
            if not udp:
                v.tcp_send_data(pickled)

            else:
                self.UDP.sendData(k, self.mapping[k].port)

    def subscribe_to_events(self):
        self.event_aggregator.subscribe(self, UpdateEvent)
        self.event_aggregator.subscribe(self, ObjectDestructionEvent)
        self.event_aggregator.subscribe(self, ObjectCreationEvent)


def connection_init(event_aggregator, config):

    connection_process = Connection(config, event_aggregator)

    # subscribe for events

    return connection_process