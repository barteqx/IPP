# -*- coding: utf-8 -*-

import abc
import core.events.event_aggregator as ea


class StateMachine(object):

    def __init__(self, event_aggregator):
        self.__state_collection = {}
        self.__current_state_key = None
        self.__current_state = None
        self.__event_aggregator = event_aggregator

    @property
    def current(self):
        return self.__current_state

    def register(self, key, state):
        if key in self.__state_collection:
            raise Exception('Specified state already exists in the state collection.')
        self.__state_collection[key] = state

    def unregister(self, key):
        if key in self.__state_collection:
            self.__state_collection.pop(key)

    def switch(self, key):
        if key not in self.__state_collection:
            raise Exception('Specified state does not exist in the state collection.')
        self.__current_state_key = key
        if self.__current_state is not None:
            self.__current_state.on_exit()
        self.__current_state = self.__state_collection[key]
        self.__current_state.on_enter()

    def start(self):
        if self.__current_state_key is None:
            raise Exception('You have to switch state machine to any state.')
        while True:
            key = self.__current_state.next()
            if key is not None and key != self.__current_state_key:
                self.switch(key)
            self.__event_aggregator.publish(ea.TickEvent())
            self.__current_state.draw()


class State(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def on_enter(self):
        pass

    def on_exit(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass
