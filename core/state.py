# -*- coding: utf-8 -*-

import abc


class StateMachine(object):

    def __init__(self):
        self.__state_collection = {}
        self.__current_state = None

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
        if self.__current_state is not None:
            self.__current_state.on_exit()
        self.__current_state = self.__state_collection[key]
        self.__current_state.on_enter()

    def start(self, key):
        self.switch(key)
        while True:
            self.__current_state.update()
            self.__current_state.draw()


class State(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, state_machine):
        self._state_machine = state_machine
        self._next_state = None

    @abc.abstractmethod
    def on_enter(self):
        pass

    def on_exit(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass
