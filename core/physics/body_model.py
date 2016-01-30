from physics_variables import *
from game.config import Config
__author__ = 'Pawel'


class BodyModel:
    #statyczny licznik modeli
    id = 0

    def __init__(self, acceleration = Acceleration(0,0), velocity = Velocity(0,0), position = Position(10,20), force = Force(0, 0), mass = 1, radius=5, type = "",this_client=False):
        self.id = BodyModel.id
        BodyModel.id += 1
        self.acceleration = acceleration
        self.velocity = velocity
        self.position = position
        self.last_position = position
        self.mass = mass
        self.radius = radius
        self.force = force
        self.type = type
        self.json = Config.get("config.json")
        self.this_client = this_client

    #returns true if object is out of map
    def update_position(self, position):
        is_out = False
        if position.x < 0 or position.x > self.json.window.size.width or position.y < 0 or position.y > self.json.window.size.height:
            is_out = True
        position.x %= self.json.window.size.width
        position.y %= self.json.window.size.height
        self.last_position = self.position
        self.position = position

        return is_out

    def __repr__(self):
        return str("Acl:(x)%d(y)%d Vel:(x)%d(y)%d Pos:(x)%d(y)%d Mass:%d R: %d" % (self.acceleration.x, self.acceleration.y,
                                                            self.velocity.x, self.velocity.y, self.position.x,
        self.position.y, self.mass, self.radius))

    def __str__(self):
        return str("Acl:(x)%.15f(y)%.15f Vel:(x)%.5f(y)%.5f Pos:(x)%d(y)%d Mass:%d R: %d force:(x)%d (y)%d" % (self.acceleration.x, self.acceleration.y,
                                                            self.velocity.x, self.velocity.y, self.position.x,
        self.position.y, self.mass, self.radius, self.force.x, self.force.y))
