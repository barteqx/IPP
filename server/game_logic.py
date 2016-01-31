__author__ = 'bartoszzasieczny'

from server_events import *

class GameLogic(object):

    def __init__(self, config, event_aggregator):
        self.config = config
        self.event_aggregator = event_aggregator
        self.subscribe_to_events()

    def notify(self, event):

        if event.type == ServerEventTypes.HANDSHAKE:
            self.add_player(event.args)

        if event.type == ServerEventTypes.QUIT:
            self.delete_player(event.args)

        if event.type == ServerEventTypes.COLLISION:
            self.delete_player(event.args)

    def add_player(self, player_data):
        pass

    def delete_player(self, player_data):
        pass

    def handle_collision(self, objects):
        pass

    def subscribe_to_events(self):
        self.event_aggregator.subscribe(self, ServerEventTypes.HANDSHAKE)
        self.event_aggregator.subscribe(self, ServerEventTypes.QUIT)
        self.event_aggregator.subscribe(self, ServerEventTypes.COLLISION)


def game_logic_init(event_aggregator, config):

    game_logic = GameLogic(config, event_aggregator)

    # subscribe for events

    return game_logic