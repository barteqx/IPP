__author__ = 'bartoszzasieczny'
from core.events.event_aggregator import *

class ServerEvent(Event):
    pass

class ServerEventTypes(object):

    HANDSHAKE = 1
    QUIT = 2
    PLAYERMOVEMENT = 3
    HANDSHAKERESPONSE = 4
    UPDATE = 5
    GAMESTATE = 6
    FORWARDEVENT = 7
    COLLISION = 9

class HandshakeEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.HANDSHAKE, args)

class QuitEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.QUIT, args)

class PlayerMovementEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.PLAYERMOVEMENT, args)

class HandshakeResponseEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.HANDSHAKERESPONSE, args)

class UpdateEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.UPDATE, args)

class GameStateEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.GAMESTATE, args)

class PlayerMovementForwardEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.FORWARDEVENT, args)

class CollisionEvent(ServerEvent):

    def __init__(self, args):
        Event.__init__(self, ServerEventTypes.COLLISION, args)