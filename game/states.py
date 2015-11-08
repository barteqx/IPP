# -*- coding: utf-8 -*-

import abc
import sys
import uuid
import pygame
import pygame.locals
import pygame.time
import core.events.event_aggregator as ea
import core.state as state


class States(object):

    Menu = 0x0001
    Battle = 0x0002
    Quit = 0x0004


class SubscribableState(state.State, ea.Subscriber):

    __metaclass__ = abc.ABCMeta

    def __init__(self, event_aggregator):
        state.State.__init__(self)
        ea.Subscriber.__init__(self, event_aggregator)
        self._uuid = uuid.uuid4()

    def uuid(self):
        return self._uuid


class MenuState(SubscribableState):

    def __init__(self, event_aggregator):
        SubscribableState.__init__(self, event_aggregator)
        self._event_aggregator.subscribe(self, ea.EventTypes.KEYDOWN)
        self._event_aggregator.subscribe(self, ea.EventTypes.QUIT)
        self.__next_state = None

    def on_enter(self):
        pass

    def next(self):
        if self.__next_state is not None:
            return self.__next_state
        return None

    def draw(self):
        import time
        print 'menu state [draw]'
        time.sleep(0.25)

    def notify(self, event):
        if isinstance(event, ea.QuitEvent):
            self.__next_state = States.Quit
        elif isinstance(event, ea.KeydownEvent):
            if event.args.key == pygame.locals.K_q:
                self.__next_state = States.Quit


class BattleState(state.State):

    def __init__(self):
        state.State.__init__(self)

    def on_enter(self):
        pass

    def next(self):
        return None

    def draw(self):
        pass


class QuitState(state.State):

    def on_enter(self):
        print 'quit state [on_enter]'
        pygame.quit()
        sys.exit()

    def on_exit(self):
        pass

    def next(self):
        return None

    def draw(self):
        pass
