__author__ = 'bartoszzasieczny'

import nympy

class PhysicalObject(Object):

    available_id = 0

    def __init__(self, position, radius, mass,  velocity = [0,0], force = [0,0]):
        self.position = numpy.array(position)
        self.radius = radius
        self.velocity = numpy.array(velocity)
        self.force = numpy.array(force)
        self.mass = mass
        self.id = PhysicalObject.available_id
        PhysicalObject.available_id += 1

    def inCollisionWith(self, object):
        if self.id == object.id:
            return false

        

