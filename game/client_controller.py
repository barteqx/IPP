from core.client.client import Client
from core.events.event_aggregator import *
import pygame
import pygame.locals
import game.config as config
from core.communication_model import PlayerMovement
import sys
__author__ = 'Pawel'

class ClientController(Subscriber):
    def __init__(self, event_aggregator):
        self.event_aggregator = event_aggregator
        self.config = config.Config.get('config.json')
        self.client = Client(self.publish, self.config.connect.host, self.config.connect.port, sys.argv[1], self.config.connect.udp_port)
        self.player_movement = PlayerMovement()
        self.client.start()
        #self.DATARECEIVED = pygame.USEREVENT + 1
        #self.data_received_event = pygame.event.Event(self.DATARECEIVED, message="DataReceived")

    def publish(self, message):
        print("publish")
        print(message)
        self.event_aggregator.publish(DataReceivedEvent(message))

    def notify(self, event):
        if isinstance(event, KeydownEvent):
            if event.args["event"].key == pygame.locals.K_UP:
                self.player_movement.moving_up = True

            if event.args["event"].key == pygame.locals.K_DOWN:
                self.player_movement.moving_down = True

            if event.args["event"].key == pygame.locals.K_LEFT:
                self.player_movement.moving_left = True

            if event.args["event"].key == pygame.locals.K_RIGHT:
                self.player_movement.moving_right = True

            self.client.handle_player_movement(self.player_movement)

        if isinstance(event, KeyupEvent):
            if event.args["event"].key == pygame.locals.K_UP:
                self.player_movement.moving_up = False

            if event.args["event"].key == pygame.locals.K_DOWN:
                self.player_movement.moving_down = False

            if event.args["event"].key == pygame.locals.K_LEFT:
                self.player_movement.moving_left = False

            if event.args["event"].key == pygame.locals.K_RIGHT:
                self.player_movement.moving_right = False

            if event.args["event"].key == pygame.locals.K_SPACE:
                self.player_movement.is_shooting = True

            self.client.handle_player_movement(self.player_movement)
        if isinstance(event, TickEvent):
            for e in self.client.get_events():
                self.publish(e)


