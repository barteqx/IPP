__author__ = 'bartoszzasieczny'

from server_events import *

class GameLogic(object):

    def __init__(self, config, publish_event_callback):
        self.config = config
        self.publish = publish_event_callback

def game_logic_init(event_aggregator, config):

    game_logic = GameLogic(config, event_aggregator.publish)

    # subscribe for events

    return game_logic