# -*- coding: utf-8 -*-

import pygame
import pygame.locals
import core.events.event_aggregator as ea
import core.events.pygame_event_loop as event_loop
import core.state as state
from game.config import Config
import game.states as states


class IPP(object):

    __allowed_pygame_events = [pygame.locals.QUIT, pygame.locals.KEYDOWN]

    def __init__(self):
        pygame.init()
        self.__event_aggregator = ea.EventAggregator()
        self.__state_machine = state.StateMachine(self.__event_aggregator)

    def run(self):
        self.__show_window()
        self.__enable_pygame_events_processing()
        self.__register_states()
        self.__state_machine.switch(states.States.Menu)
        self.__state_machine.start()

    def __show_window(self):
        Context.screen = Window().show()

    def __enable_pygame_events_processing(self):
        pygame_event_loop = event_loop.PygameEventLoop(self.__event_aggregator)
        pygame_event_loop.set_allowed_events(IPP.__allowed_pygame_events)
        pygame_event_loop.on()

    def __register_states(self):
        self.__state_machine.register(states.States.Menu, states.MenuState(self.__event_aggregator))
        self.__state_machine.register(states.States.Quit, states.QuitState())


class Context(object):

    screen = None
    config = Config.get('config.json')


class Window(object):

    def show(self):
        return self.__prepare_screen()

    def __prepare_screen(self):
        pygame.display.set_caption(Context.config.game.name)
        screen = pygame.display.set_mode(
            (Context.config.window.size.width, Context.config.window.size.height)
        )
        return screen
