__author__ = 'bartoszzasieczny'


class PhysicsUpdate:
    def __init__(self, objects_states, objects_to_delete):
        self.objects_states = objects_states
        self.objects_to_delete = objects_to_delete


class PlayerMovement:
    def __init__(self):
        self.moving_right    = False
        self.right_force_set = False
        self.right_force_subtraction = False
        self.moving_left     = False
        self.left_force_set  = False
        self.left_force_subtraction = False
        self.moving_up       = False
        self.up_force_set    = False
        self.up_force_subtraction = False
        self.moving_down     = False
        self.down_force_set  = False
        self.down_force_subtraction = False


class PlayerDescription:
    def __init__(self, name, udp_port):
        self.name = name
        self.udp_port = udp_port


class PlayerQuit:
    pass

class PlayerJoin:
    def __init__(self, list_of_players):
        self.list_of_players = list_of_players

class ObjectCreation:
    def __init__(self, game_object, object_type):
        self.object = game_object
        self.object_type = object_type


class ObjectDestruction:
    def __init__(self, id):
        self.id = id

class HandshakeResponse:
    def __init__(self, obj, ok=True):
        self.obj = obj
        self.ok = ok