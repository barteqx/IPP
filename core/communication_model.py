__author__ = 'bartoszzasieczny'

class PhysicsUpdate:
    def __init(self, objects_states, objects_to_delete):
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
    def __init__(self, name):
        self.name = name
