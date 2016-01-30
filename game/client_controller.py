from core.client.client import Client
from core.events.event_aggregator import *
import pygame
import pygame.locals
import game.config as config
from core.communication_model import PlayerMovement

__author__ = 'Pawel'

class ClientController(Subscriber):
    def __init__(self, event_aggregator):
        self.event_aggregator = event_aggregator
        self.config = config.Config.get('config.json')
        self.client = Client(self.publish, self.config.connect.host, self.config.connect.port)
        self.player_movement = PlayerMovement(False, False, False, False, False)
        self.client.start()
        #self.DATARECEIVED = pygame.USEREVENT + 1
        #self.data_received_event = pygame.event.Event(self.DATARECEIVED, message="DataReceived")

    def publish(self, message):
        self.event_aggregator.publish(DataReceivedEvent(message))

    def notify(self, event):
        if isinstance(event, KeydownEvent):
            if event.args.key == pygame.locals.K_UP:
                self.player_movement.moving_up = True

            if event.args.key == pygame.locals.K_DOWN:
                self.player_movement.moving_down = True

            if event.args.key == pygame.locals.K_LEFT:
                self.player_movement.moving_left = True

            if event.args.key == pygame.locals.K_RIGHT:
                self.player_movement.moving_right = True

            self.client.handle_player_movement(self.player_movement)

        if isinstance(event, KeyupEvent):
            if event.args.key == pygame.locals.K_UP:
                self.player_movement.moving_up = False

            if event.args.key == pygame.locals.K_DOWN:
                self.player_movement.moving_down = False

            if event.args.key == pygame.locals.K_LEFT:
                self.player_movement.moving_left = False

            if event.args.key == pygame.locals.K_RIGHT:
                self.player_movement.moving_right = False

            if event.args.key == pygame.locals.K_SPACE:
                self.player_movement.is_shooting = True

            self.client.handle_player_movement(self.player_movement)


