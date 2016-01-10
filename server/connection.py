__author__ = 'bartoszzasieczny'
from twisted.internet import reactor

from server_events import *
from tcp_connection import *
from udp_communication import *

class Connection(object):

    def __init__(self, config, publish_event_callback):
        self.config = config
        self.publish = publish_event_callback

def connection_init(event_aggregator, config):

    connection_process = Connection(config, event_aggregator.publish)

    # subscribe for events

    return connection_process