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
            id = 0
            if event.args["ip"] != -1:
                id = event.args["id"]
            else:
                id = self.view.model.this_client_id

            if event.args["event"].key == pygame.locals.K_UP:
                self.view.model.player_movement_dict[id].moving_up = True

            if event.args["event"].key == pygame.locals.K_DOWN:
                self.view.model.player_movement_dict[id].moving_down = True

            if event.args["event"].key == pygame.locals.K_LEFT:
                self.view.model.player_movement_dict[id].moving_left = True

            if event.args["event"].key == pygame.locals.K_RIGHT:
                self.view.model.player_movement_dict[id].moving_right = True

        if isinstance(event, KeyupEvent):
            id = 0
            if event.args["ip"] != -1:
                id = event.args["id"]
            else:
                id = self.view.model.this_client_id

            if event.args["event"].key == pygame.locals.K_UP:
                self.view.model.player_movement_dict[id].moving_up = False
                self.view.model.player_movement_dict[id].up_force_set = False
                self.view.model.player_movement_dict[id].up_force_subtraction = True

            if event.args["event"].key == pygame.locals.K_DOWN:
                self.view.model.player_movement_dict[id].moving_down = False
                self.view.model.player_movement_dict[id].down_force_set = False
                self.view.model.player_movement_dict[id].down_force_subtraction = True

            if event.args["event"].key == pygame.locals.K_LEFT:
                self.view.model.player_movement_dict[id].moving_left = False
                self.view.model.player_movement_dict[id].left_force_set = False
                self.view.model.player_movement_dict[id].left_force_subtraction = True

            if event.args["event"].key == pygame.locals.K_RIGHT:
                self.view.model.player_movement_dict[id].moving_right    = False
                self.view.model.player_movement_dict[id].right_force_set = False
                self.view.model.player_movement_dict[id].right_force_subtraction = True

            if event.args["event"].key == pygame.locals.K_SPACE:
                self.view.model.shoot()

        if isinstance(event, DataReceivedEvent):
            print("player controller")
            print(event)
            print event.args
            if event.args.__class__.__name__ == "PhysicsUpdate":
                self.view.model.server_update_objects(event.args.objects_states)

            if event.args.__class__.__name__ == "HandshakeResponse":
                print event.args.obj
                self.view.model.set_this_client_id(event.args.obj)

