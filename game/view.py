import pygame
from core.physics.body_model import *
from model import *
import sys
__author__ = 'Pawel'

class View:
    def __init__(self):
        self.model = Model()
        self.font = self.make_font(15)
        self.text = self.font.render(sys.argv[1], True, (0, 128, 0))
    def render_battle_state(self, delta_time, screen):
        self.model.update_battle_state(delta_time)
        for model in self.model.list_of_players:
            pygame.draw.circle(screen, (0, 0, 255), (int(model.position.x), int(model.position.y)), model.radius)
            if(model.this_client):
                screen.blit(self.text,(model.position.x - self.text.get_width() // 2, (model.position.y - model.radius)- self.text.get_height() // 2))
        for model in self.model.list_of_planets:
            pygame.draw.circle(screen, (0, 255, 255), (int(model.position.x), int(model.position.y)), model.radius)
        for model in self.model.list_of_shots:
            pygame.draw.circle(screen, (255, 255, 255), (int(model.position.x), int(model.position.y)), model.radius)

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
