# -*- coding: utf-8 -*-

import pygame
import pygame.locals
from core.state import StateMachine
from game.config import Config
from game.states import States, MenuState, QuitState


class IPP(object):

    def __init__(self):
        self.__window = Window()
        self.__state_machine = StateMachine()
        self.__state_machine.register(States.Menu, MenuState())
        self.__state_machine.register(States.Quit, QuitState())

    def run(self):
        self.__window.display()
        self.__state_machine.switch(States.Menu)
        self.__state_machine.start()


class Context(object):

    pass


class Window(object):

    def __init__(self):
        self.__config = Config.get('config.json')

    def display(self):
        self.__prepare_screen()

    def __prepare_screen(self):
        pygame.init()
        pygame.display.set_caption(self.__config.game.name)
        pygame.event.set_allowed(None)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
        pygame.display.set_mode((self.__config.window.size.width, self.__config.window.size.height))
