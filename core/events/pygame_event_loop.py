# -*- coding: utf-8 -*-

import pygame
import pygame.locals
import core.events.event_aggregator as ea


class PygameEventLoop(ea.Subscriber):

    def __init__(self, event_aggregator):
        self.__event_aggregator = event_aggregator

    def set_allowed_events(self, events):
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(events)

    def on(self):
        self.__event_aggregator.subscribe(self, ea.EventTypes.TICK)

    def off(self):
        self.__event_aggregator.unsubscribe(self, ea.EventTypes.TICK)

    def notify(self, event):
        if isinstance(event, ea.TickEvent):
            self.__process_events()

    def __process_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.locals.QUIT:
                self.__event_aggregator.publish(ea.QuitEvent())
            elif event.type == pygame.locals.KEYDOWN:
                self.__event_aggregator.publish(ea.KeydownEvent(event))
            elif event.type == pygame.locals.KEYUP:
                self.__event_aggregator.publish(ea.KeyupEvent(event))
