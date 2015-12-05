from physics_variables import *
__author__ = 'Pawel'


class BodyModel:
    #statyczny licznik modeli
    id = 0

    def __init__(self, acceleration = Acceleration(0,0), velocity = Velocity(0,0), position = Position(10,20), mass = 1, radius=5):
        self.id = BodyModel.id
        BodyModel.id += 1
        self.acceleration = acceleration
        self.velocity = velocity
        self.position = position
        self.last_position = position
        self.mass = mass
        self.radius = radius

    def update_position(self, position):
        self.last_position = self.position
        self.position = position
    def __repr__(self):
        return str("Acl:(x)%d(y)%d Vel:(x)%d(y)%d Pos:(x)%d(y)%d Mass:%d R: %d" % (self.acceleration.x, self.acceleration.y,
                                                            self.velocity.x, self.velocity.y, self.position.x,
        self.position.y, self.mass, self.radius))
    def __str__(self):
        return str("Acl:(x)%d(y)%d Vel:(x)%d(y)%d Pos:(x)%d(y)%d Mass:%d R: %d" % (self.acceleration.x, self.acceleration.y,
                                                            self.velocity.x, self.velocity.y, self.position.x,
        self.position.y, self.mass, self.radius))
