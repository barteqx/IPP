from core.physics.body_model import *
from core.physics.physics import Physics
__author__ = 'Pawel'


class Model:
    def __init__(self):
        self.list_of_players = []
        self.list_of_planets = []
        self.list_of_shots   = []
        self.list_of_battle_objects = []

        self.moving_right    = False
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
        self.down_force_subtraction = False

        self.move_speed = 10**6
        self.force_move_addition = 10**6

        self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(100, 200), Force(0, 0), 1000, 25))
        self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(200, 300), Force(0, 0), 10, 25))
        self.list_of_planets.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(300, 200), Force(0, 0), 10**13, 25))

        self.list_of_battle_objects.append(self.list_of_players)
        self.list_of_battle_objects.append(self.list_of_planets)
        self.list_of_battle_objects.append(self.list_of_shots)

    def update_battle_state(self, delta_time):
        self.control_service()
        Physics.compute_gravity_influence(self.list_of_battle_objects, delta_time)
        self.list_of_players = self.list_of_battle_objects[0]
        self.list_of_planets = self.list_of_battle_objects[1]
        self.list_of_shots   = self.list_of_battle_objects[2]

    def control_service(self):
        if self.moving_right:
            if self.right_force_set is not True:
                self.list_of_players[0].force.x += self.force_move_addition
                self.right_force_set = True

        if self.right_force_subtraction:
            self.list_of_players[0].force.x -= self.force_move_addition
            self.right_force_subtraction = False

        if self.moving_left:
            if self.left_force_set is not True:
                self.list_of_players[0].force.x -= self.force_move_addition
                self.left_force_set = True

        if self.left_force_subtraction:
            self.list_of_players[0].force.x += self.force_move_addition
            self.left_force_subtraction = False

        if self.moving_down:
            if self.down_force_set is not True:
                self.list_of_players[0].force.y += self.force_move_addition
                self.down_force_set = True

        if self.down_force_subtraction:
            self.list_of_players[0].force.y -= self.force_move_addition
            self.down_force_subtraction = False

        if self.moving_up:
            if self.up_force_set is not True:
                self.list_of_players[0].force.y -= self.force_move_addition
                self.up_force_set = True

        if self.up_force_subtraction:
            self.list_of_players[0].force.y += self.force_move_addition
            self.up_force_subtraction = False
