import pygame
from core.physics.body_model import *
from model import *
import sys
__author__ = 'Pawel'

class View:
    def __init__(self):
        self.model = Model()
        self.font = self.make_font(15)
        self.names = {}
        self.init_names()
        self.text = self.font.render(sys.argv[1], True, (0, 128, 0))

    def render_battle_state(self, delta_time, screen):
        self.model.update_battle_state(delta_time)
        for model in self.model.list_of_players:
            pygame.draw.circle(screen, (0, 0, 255), (int(model.position.x), int(model.position.y)), model.radius)
            if model.name in self.names:
                screen.blit(self.names[model.name], (model.position.x - self.text.get_width() // 2, (model.position.y - model.radius)- self.text.get_height() // 2))
        for model in self.model.list_of_planets:
            pygame.draw.circle(screen, (0, 255, 255), (int(model.position.x), int(model.position.y)), model.radius)
        for model in self.model.list_of_shots:
            pygame.draw.circle(screen, (255, 255, 255), (int(model.position.x), int(model.position.y)), model.radius)
        h = 0
        for text, name in self.names.items():
            screen.blit(name, (0, 0 + h))
            h += 20

    def init_names(self, list_of_players=None):
        if list_of_players:
            self.model.list_of_players = list_of_players
            print list_of_players
        for player in self.model.list_of_players:
            self.names[player.name] = self.font.render(player.name, True, (0, 128, 0))

    def make_font(self, size):
        available = pygame.font.get_fonts()
        fonts = [
        "Bizarre-Ass Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]
        choices = map(lambda x:x.lower().replace(' ', ''), fonts)
        for choice in choices:
            if choice in available:
                return pygame.font.SysFont(choice, size)
        return pygame.font.Font(None, size)
