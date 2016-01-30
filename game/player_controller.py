from core.events.event_aggregator import *
import pygame
import pygame.locals
__author__ = 'Pawel'

from core.communication_model import PhysicsUpdate

class PlayerController(Subscriber):
    def __init__(self, view):
        self.view = view
        #self.client = client
    def notify(self, event):
        if isinstance(event, KeydownEvent):
            if event.args.key == pygame.locals.K_UP:
                self.view.model.moving_up = True

            if event.args.key == pygame.locals.K_DOWN:
                self.view.model.moving_down = True

            if event.args.key == pygame.locals.K_LEFT:
                self.view.model.moving_left = True

            if event.args.key == pygame.locals.K_RIGHT:
                self.view.model.moving_right = True

        if isinstance(event, KeyupEvent):
            if event.args.key == pygame.locals.K_UP:
                self.view.model.moving_up = False
                self.view.model.up_force_set = False
                self.view.model.up_force_subtraction = True

            if event.args.key == pygame.locals.K_DOWN:
                self.view.model.moving_down = False
                self.view.model.down_force_set = False
                self.view.model.down_force_subtraction = True

            if event.args.key == pygame.locals.K_LEFT:
                self.view.model.moving_left = False
                self.view.model.left_force_set = False
                self.view.model.left_force_subtraction = True

            if event.args.key == pygame.locals.K_RIGHT:
                self.view.model.moving_right    = False
                self.view.model.right_force_set = False
                self.view.model.right_force_subtraction = True

            if event.args.key == pygame.locals.K_SPACE:
                self.view.model.shoot()

        if isinstance(event, DataReceivedEvent):
            if DataReceivedEvent.args[0].__class__.__name__ == "PhysicsUpdate":
                self.view.model.server_udpate_objects(DataReceivedEvent.args[0])
