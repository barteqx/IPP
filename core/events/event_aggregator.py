# -*- coding: utf-8 -*-

import weakref
import abc


class EventAggregator(object):

    def __init__(self):
        self.__event_subscribers = {}

    def subscribe(self, subscriber, event_type):
        if event_type not in self.__event_subscribers:
            self.__event_subscribers[event_type] = weakref.WeakValueDictionary()
        subscriber_id = id(subscriber)
        self.__event_subscribers[event_type][subscriber_id] = subscriber

    def unsubscribe(self, subscriber, event_type):
        subscriber_id = id(subscriber)
        del self.__event_subscribers[event_type][subscriber_id]

    def publish(self, event):
        subscribers = self.__event_subscribers[event.type]
        for subscriber in subscribers.itervaluerefs():
            subscriber().notify(event)


class Subscriber(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def notify(self, event):
        pass


class Event(object):

    def __init__(self, type, args=None):
        self.__type = type
        self.__args = args

    @property
    def type(self):
        return self.__type

    @property
    def args(self):
        return self.__args


class EventTypes(object):

    TICK = 0x0001
    QUIT = 0x0002
    KEYDOWN = 0x0004


class TickEvent(Event):

    def __init__(self):
        Event.__init__(self, EventTypes.TICK)


class QuitEvent(Event):

    def __init__(self):
        Event.__init__(self, EventTypes.QUIT)


class KeydownEvent(Event):

    def __init__(self, args):
        Event.__init__(self, EventTypes.KEYDOWN, args)
