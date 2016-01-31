from server.physics import *
from server.connection import *
from game.config import *
from core.events.event_aggregator import *


class Server(object):

    def __init__(self):
        self.__config = Config.get("server_config.json")
        self.__event_aggregator = EventAggregator()
        self.physics = physics_init(self.__event_aggregator, self.__config)
        self.connection = connection_init(self.__event_aggregator, self.__config)

    def runserver(self):
        self.physics.start()
        self.connection.set_up_connection()


if __name__ == "__main__":
    Server().runserver()
