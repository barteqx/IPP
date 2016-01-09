__author__ = 'bartoszzasieczny'
from multiprocessing import Process

from core.physics.physics import *
from server_events import *

class PhysicsProcess(Process):

    def __init__(self, config, publish_event_callback):
        Process.__init__(self)
        self.config = config
        self.publish = publish_event_callback

def physics_init(event_aggregator, config):

    physics_process = PhysicsProcess(config, event_aggregator.publish)

    # subscribe for events

    return physics_process
