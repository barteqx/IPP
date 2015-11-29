import pygame
from core.physics.body_model import *
from model import *
__author__ = 'Pawel'

class View:
    def __init__(self):
        self.model = Model()

    def render_battle_state(self, delta_time, screen):
        self.model.update_battle_state(delta_time)
        for model in self.model.list_of_players:
            pygame.draw.circle(screen, (0, 0, 255), (int(model.position.x), int(model.position.y)), model.radius)
        for model in self.model.list_of_planets:
            pygame.draw.circle(screen, (0, 255, 255), (int(model.position.x), int(model.position.y)), model.radius)
        for model in self.model.list_of_shots:
            pygame.draw.circle(screen, (255, 255, 255), (int(model.position.x), int(model.position.y)), model.radius)
