# -*- coding: utf-8 -*-

import abc
import sys
import pygame
import pygame.locals
import pygame.time
import core.events.event_aggregator as ea
import core.state as state
import game.ipp


class States(object):

    Menu = 0x0001
    Battle = 0x0002
    Quit = 0x0004


class State(state.State, ea.Subscriber):

    __metaclass__ = abc.ABCMeta

    def __init__(self, event_aggregator):
        state.State.__init__(self)
        self.__show_fps = False
        self._event_aggregator = event_aggregator
        self._context = game.ipp.Context
        self._screen = game.ipp.Context.screen
        self._display = pygame.display
        self._clock = pygame.time.Clock()

    def on_enter(self):
        self._event_aggregator.subscribe(self, ea.EventTypes.KEYDOWN)

    def on_exit(self):
        self._event_aggregator.unsubscribe(self, ea.EventTypes.KEYDOWN)

    def draw(self):
        self._display.update()
        self._clock.tick(self._context.config.game.fps)
        self._screen.fill(self._context.background_color)
        if self.__show_fps:
            self.__draw_fps_stats()

    def notify(self, event):
        if isinstance(event, ea.KeydownEvent):
            if event.args.key == pygame.locals.K_F5:
                self.__show_fps = not self.__show_fps

    def __draw_fps_stats(self):
        fps = int(self._clock.get_fps())
        text = self._context.font_small.render('FPS: {0}'.format(fps), 1, (255, 255, 255))
        text_pos = text.get_rect()
        text_pos.left = 5
        text_pos.top = self._screen.get_rect().height - text_pos.height - 5
        self._screen.blit(text, text_pos)


class MenuState(State):

    def __init__(self, event_aggregator):
        State.__init__(self, event_aggregator)
        self.__next_state = None

    def on_enter(self):
        State.on_enter(self)
        self._event_aggregator.subscribe(self, ea.EventTypes.QUIT)

    def on_exit(self):
        State.on_exit(self)
        self._event_aggregator.unsubscribe(self, ea.EventTypes.QUIT)

    def next(self):
        if self.__next_state is not None:
            return self.__next_state
        return None

    def draw(self):
        State.draw(self)

    def notify(self, event):
        State.notify(self, event)
        if isinstance(event, ea.QuitEvent):
            self.__next_state = States.Quit
        elif isinstance(event, ea.KeydownEvent):
            if event.args.key == pygame.locals.K_q:
                self.__next_state = States.Quit


class BattleState(State):

    def __init__(self, event_aggregator):
        State.__init__(self, event_aggregator)

    def on_enter(self):
        pass

    def next(self):
        return None

    def draw(self):
        pass

    def notify(self, event):
        pass


class QuitState(state.State):

    def on_enter(self):
        pygame.quit()
        sys.exit()

    def on_exit(self):
        pass

    def next(self):
        return None

    def draw(self):
        pass
