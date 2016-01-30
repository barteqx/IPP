__author__ = 'bartoszzasieczny'


class PhysicsUpdate:
    def __init__(self, objects_states, objects_to_delete):
        self.objects_states = objects_states
        self.objects_to_delete = objects_to_delete


class PlayerMovement:
    def __init__(self, moving_right, moving_left, moving_up, moving_down, is_shooting):
        self.moving_right = moving_right
        self.moving_left = moving_left
        self.moving_up = moving_up
        self.moving_down = moving_down
        self.is_shooting = is_shooting


class PlayerDescription:
    def __init__(self, name, udp_port):
        self.name = name
        self.udp_port = udp_port


class PlayerQuit:
    pass


class ObjectCreation:
    def __init__(self, game_object, object_type):
        self.object = game_object
        self.object_type = object_type


class ObjectDestruction:
    def __init__(self, id):
        self.id = id

class HandshakeResponse:
    def __init__(self, id, ok=True):
        self.id = id
        self.ok = ok