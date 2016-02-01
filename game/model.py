from core.physics.body_model import *
from core.physics.physics import Physics
from core.communication_model import PlayerMovement
import collections
import sys
import math
__author__ = 'Pawel'

class Model:
    def __init__(self):
        self.list_of_players = []
        self.list_of_planets = []
        self.list_of_shots   = []
        self.list_of_battle_objects = []

        self.player_movement_dict = collections.defaultdict(self.default_value_for_md)

        """self.moving_right    = False
        self.right_force_set = False
        self.right_force_subtraction = False
        self.moving_left     = False
        self.left_force_set  = False
        self.left_force_subtraction = False
        self.moving_up       = False
        self.up_force_set    = False
        self.up_force_subtraction = False
        self.moving_down     = False
        self.down_force_set  = False
        self.down_force_subtraction = False"""

        self.move_speed = 10**6
        self.force_move_addition = 10**6

        self.shoot_x_speed = 700
        self.shoot_y_speed = 700

        self.shoot_radius = 2
        self.json = Config.get("config.json")
        self.width = self.json.window.size.width
        self.height = self.json.window.size.height

        self.this_client_id = 0

        """self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(100, 200), Force(0, 0), 1000, 25, "player", True, self.width, self.height))
        self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(200, 300), Force(0, 0), 10, 25,"player", False, self.width, self.height))
        #self.list_of_planets.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(300, 200), Force(0, 0), 10**13, 25))
        self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(600, 200), Force(1000, 0), 1000, 25,"player", False, self.width, self.height))
        self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(500, 300), Force(-100, 50), 10, 25, "player", False, self.width, self.height))
        #self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(300, 200), Force(50, 50), 1000, 25))
        #self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(400, 300), Force(10, 10), 10, 25))

        self.list_of_planets.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(300, 200), Force(50, 50), 1000, 25, "planet", False, self.width, self.height))
        self.list_of_planets.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(400, 300), Force(10, 10), 10, 25, "planet", False, self.width, self.height))"""

        self.list_of_battle_objects.append(self.list_of_players)
        self.list_of_battle_objects.append(self.list_of_planets)
        self.list_of_battle_objects.append(self.list_of_shots)

    def default_value_for_md(self):
        return PlayerMovement()

    def update_battle_state(self, delta_time):
        #self.control_service()
        Physics.compute_gravity_influence(self.list_of_battle_objects, delta_time, self.player_movement_dict)
        self.list_of_players = self.list_of_battle_objects[0]
        self.list_of_planets = self.list_of_battle_objects[1]
        self.list_of_shots   = self.list_of_battle_objects[2]


    def shoot(self):
        p = None
        for player in self.list_of_players:
            if player.id == self.this_client_id:
                p = player
        #p = self.list_of_players[0]
        R = p.radius
        r = self.shoot_radius
        vx = vy = appx = appy = 0
        if self.player_movement_dict[p.id].moving_right:
            vx += self.shoot_x_speed
            appx += r + R + 2
        if self.player_movement_dict[p.id].moving_left:
            vx -= self.shoot_x_speed
            appx -= r + R + 2
        if self.player_movement_dict[p.id].moving_down:
            vy += self.shoot_y_speed
            appy += r + R + 2
        if self.player_movement_dict[p.id].moving_up:
            vy -= self.shoot_y_speed
            appy -= r + R + 2
        if vx != 0 or vy != 0:
            self.list_of_shots.append(BodyModel(Acceleration(0, 0), Velocity(vx, vy), Position(p.position.x + appx
                                                                           ,p.position.y + appy), Force(0, 0), 1, r, "shoot", False, self.width, self.height))

    def control_service(self):
        p = None
        print self.this_client_id
        for player in self.list_of_players:
            if player.id == self.this_client_id:
                p = player
        if not p:
            return
        if self.player_movement_dict[p.id].moving_right:
            if self.player_movement_dict[p.id].right_force_set is not True:
                p.force.x += self.force_move_addition
                self.player_movement_dict[p.id].right_force_set = True

        if self.player_movement_dict[p.id].right_force_subtraction:
            p.force.x -= self.force_move_addition
            self.player_movement_dict[p.id].right_force_subtraction = False

        if self.player_movement_dict[p.id].moving_left:
            if self.player_movement_dict[p.id].left_force_set is not True:
                p.force.x -= self.force_move_addition
                self.player_movement_dict[p.id].left_force_set = True

        if self.player_movement_dict[p.id].left_force_subtraction:
            p.force.x += self.force_move_addition
            self.player_movement_dict[p.id].left_force_subtraction = False

        if self.player_movement_dict[p.id].moving_down:
            if self.player_movement_dict[p.id].down_force_set is not True:
                p.force.y += self.force_move_addition
                self.player_movement_dict[p.id].down_force_set = True

        if self.player_movement_dict[p.id].down_force_subtraction:
            p.force.y -= self.force_move_addition
            self.player_movement_dict[p.id].down_force_subtraction = False

        if self.player_movement_dict[p.id].moving_up:
            if self.player_movement_dict[p.id].up_force_set is not True:
                p.force.y -= self.force_move_addition
                self.player_movement_dict[p.id].up_force_set = True

        if self.player_movement_dict[p.id].up_force_subtraction:
            p.force.y += self.force_move_addition
            self.player_movement_dict[p.id].up_force_subtraction = False

    def server_update_objects(self, list_of_objects):
        #print("server_update_objects")
        #print(len(list_of_objects[1]))
        self.list_of_battle_objects[0] = list_of_objects[0]
        self.list_of_battle_objects[1] = list_of_objects[1]
        self.list_of_battle_objects[2] = list_of_objects[2]
        #print(len(self.list_of_battle_objects[1]))

    def set_this_client_id(self, obj):
        #print("set this client id")
        self.this_client_id = obj.id
        self.list_of_players.append(obj)

        #self.list_of_players.append(BodyModel(a, v, p, f, mass, 25,
        #                                      "player", True, obj.width, obj.height, port = obj.port, addr = obj.addr))
        #self.list_of_players[0].id = obj.id
