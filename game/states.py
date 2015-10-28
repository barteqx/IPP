# -*- coding: utf-8 -*-

import sys
import pygame
import pygame.locals
import pygame.time
from core.state import State


class States(object):
    Menu = 0x0001
    Quit = 0x0002


class MenuState(State):

    def __init__(self, state_machine):
        State.__init__(self, state_machine)
        self.__clock = pygame.time.Clock()

    def on_enter(self):
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_q:
                    self._state_machine.switch(States.Quit)

    def draw(self):
        import time
        print 'menu state [draw]'
        time.sleep(0.25)


class QuitState(State):

    def __init__(self, state_machine):
        State.__init__(self, state_machine)

    def on_enter(self):
        print 'quit state [on_enter]'
        pygame.quit()
        sys.exit()

    def on_exit(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass
