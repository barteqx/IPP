__author__ = 'Pawel'


class Force:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str("force.x: %.20f force.y: %.20f" % (self.x, self.y))
class Acceleration:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str("acceleration.x: %d acceleration.y: %d" % (self.x, self.y))

class Velocity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str("velocity.x: %.20f velocity.y: %.20f" % (self.x, self.y))
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str("position.x: %d position.y: %d" % (self.x, self.y))