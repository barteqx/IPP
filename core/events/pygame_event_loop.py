# -*- coding: utf-8 -*-

import pygame
import pygame.locals
import uuid
import core.events.event_aggregator as ea


class PygameEventLoop(ea.Subscriber):

    def __init__(self, event_aggregator):
        super(PygameEventLoop, self).__init__(event_aggregator)
        self.__uuid = uuid.uuid4()

    def set_allowed_events(self, events):
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(events)

    def on(self):
        self._event_aggregator.subscribe(self, ea.EventTypes.TICK)

    def off(self):
        self._event_aggregator.unsubscribe(self, ea.EventTypes.TICK)

    def uuid(self):
        return self.__uuid

    def notify(self, event):
        if isinstance(event, ea.TickEvent):
            self.__process_events()

    def __process_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.locals.QUIT:
                self._event_aggregator.publish(ea.QuitEvent())
            elif event.type == pygame.locals.KEYDOWN:
                self._event_aggregator.publish(ea.KeydownEvent(event))
