__author__ = 'bartoszzasieczny'
from core.events.event_aggregator import *

class ServerEvent(Event):
    pass

class ServerEventTypes(object):

    HANDSHAKE = 1
    QUIT = 2
    KEYDOWN = 3
    KEYUP = 4
    UPDATE = 5
    GAMESTATE = 6
    OBJECTCREATION = 7
    OBJECTDESTRUCTION = 8
    COLLISION = 9

class HandshakeEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.HANDSHAKE, args)

class QuitEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.QUIT, args)

class KeydownEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.KEYDOWN, args)

class KeyupEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.KEYUP, args)

class UpdateEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.UPDATE, args)

class GameStateEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.GAMESTATE, args)

class ObjectCreationEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.OBJECTCREATION, args)

class ObjectDestructionEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.OBJECTDESTRUCTION, args)

class CollisionEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.COLLISION, args)