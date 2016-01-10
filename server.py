from server.physics import *
from server.connection import *
from server.game_logic import *
from game.config import *
from core.events.event_aggregator import *


class Server(object):

    def __init__(self):
        self.__config = Config.get("server_config.json")
        self.__event_aggregator = EventAggregator()
        self.physics = physics_init(self.__event_aggregator, self.__config)
        self.connection = connection_init(self.__event_aggregator, self.__config)
        self.game_logic = game_logic_init(self.__event_aggregator, self.__config)

    def runserver(self):
        print "Running physics"
        self.physics.start()


if __name__ == "__main__":
    Server().runserver()
