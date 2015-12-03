from core.physics.body_model import *
from core.physics.physics import Physics
__author__ = 'Pawel'


class Model:
    def __init__(self):
        self.list_of_players = []
        self.list_of_planets = []
        self.list_of_shots   = []
        self.list_of_battle_objects = []

        self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(100, 200), 1000, 50))
        self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(200, 300), 10, 50))

        self.list_of_planets.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(300, 200), 10**17, 500))

        self.list_of_battle_objects.append(self.list_of_players)
        self.list_of_battle_objects.append(self.list_of_planets)
        self.list_of_battle_objects.append(self.list_of_shots)

    def update_battle_state(self, delta_time):
        self.list_of_battle_objects = Physics.compute_gravity_influence(self.list_of_battle_objects, delta_time)
        self.list_of_players = self.list_of_battle_objects[0]
        self.list_of_planets = self.list_of_battle_objects[1]
        self.list_of_shots   = self.list_of_battle_objects[2]