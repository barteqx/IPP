from physics_variables import *
__author__ = 'Pawel'


class BodyModel:
    #statyczny licznik modeli
    id = 0

    def __init__(self, acceleration = Acceleration(0,0), velocity = Velocity(0,0), position = Position(0,0), mass = 0, radius=0):
        BodyModel.id += 1
        self.acceleration = acceleration
        self.velocity = velocity
        self.position = position
        self.mass = mass
        self.radius
