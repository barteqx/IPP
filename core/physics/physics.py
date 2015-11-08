from body_model import *
import math
import numpy as np
__author__ = 'Pawel'


class Physics:
    constG = 6.67 * 10**-11

    def __init__(self):
        print Physics.constG
    #zakladam ze kazdy objekt bedzie mial informacje o swoim id, polozeniu, masie, aktualnej predkosci oraz pozycji
    #funkcja zwraca list� obiekt�w z zaktualizowanymi zmiennymi
    @staticmethod
    def compute_gravity_influence(listOfObjects, deltaTime):
        #lista, w kotrej znajda sie zaktualizowane dane obiektow
        resultListOfObjects = []

        for obj in listOfObjects:
            force = Physics.computeForce(listOfObjects, obj)
            acceleration = Physics.computeAcceleration(force, obj.mass)
            velocity = Physics.computeVelocity(obj.velocity, acceleration, deltaTime)
            position = Physics.computePosition(obj.position, velocity, deltaTime)

            resultListOfObjects.append(BodyModel(acceleration, velocity, position, obj.mass))

        return resultListOfObjects

    @staticmethod
    def __compute_acceleration(force, mass):
        acceleration = Acceleration(0,0)
        if mass != 0:
            acceleration.x = force.x/mass
            acceleration.y = force.y/mass

        return acceleration

    @staticmethod
    def __compute_velocity(oldVelocity, acceleration, deltaTime):
        velocity = Velocity(oldVelocity.x, oldVelocity.y)
        velocity.x += acceleration.x * deltaTime
        velocity.y += acceleration.y * deltaTime

        return velocity

    @staticmethod
    def __compute_position(oldPosition, velocity, deltaTime):
        position = Position(oldPosition.x, oldPosition.y)
        position.x += velocity.x * deltaTime
        position.y += velocity.y * deltaTime

        return position

    @staticmethod
    def __compute_force(listOfObjects, obj1):
        force = Force(0,0)
        for obj2 in listOfObjects:
            r = math.sqrt((obj1.position.x - obj2.position.x)**2 + (obj1.position.y - obj2.position.y)**2)
            if r != 0:
                force.x += Physics.constG * obj1.mass * obj2.mass * (obj1.position.x - obj2.position.x) / r**3
                force.y += Physics.constG * obj1.mass * obj2.mass * (obj1.position.y - obj2.position.y) / r**3

        return

    @staticmethod
    def __detect_collision(obj1, obj2):
        v_obj1 = np.array([obj1.position.x, obj1.position.y])
        v_obj2 = np.array([obj2.position.x, obj2.position.y])

        v_normal = np.array([v_obj1[0] - v_obj2[0], v_obj1[1] - v_obj2[1]])

        if np.absolute(v_normal) <= (obj1.radius + obj2.radius):
            return True
        else: return False

    @staticmethod
    def  __compute_velocities_at_collision(obj1, obj2):

        v_obj1 = np.array([obj1.velocity.x, obj1.velocity.y])
        v_obj2 = np.array([obj2.velocity.x, obj2.velocity.y])

        v_normal = np.array([v_obj1[0] - v_obj2[0], v_obj1[1] - v_obj2[1]])
        v_unit_normal = np.divide(v_normal, np.absolute(v_normal))
        v_unit_tangent = np.array([-1*v_unit_normal[1], v_unit_normal[0]])

        v_obj1_normal  = np.vdot(v_unit_normal, v_obj1)
        v_obj1_tangent = np.vdot(v_unit_tangent, v_obj1)
        v_obj2_normal  = np.vdot(v_unit_normal, v_obj2)
        v_obj2_tangent = np.vdot(v_unit_tangent, v_obj2)

        v_obj1_new_normal = (v_obj1_normal(obj1.mass - obj2.mass) + 2*obj2.mass*v_obj2_normal)/(obj1.mass + obj2.mass)
        v_obj2_new_normal = (v_obj2_normal(obj2.mass - obj1.mass) + 2*obj1.mass*v_obj1_normal)/(obj1.mass + obj2.mass)

        vec_obj1_normal  = np.dot(v_obj1_new_normal, v_unit_normal)
        vec_obj1_tangent = np.dot(v_obj1_tangent, v_unit_tangent)
        vec_obj2_normal  = np.dot(v_obj2_new_normal, v_unit_normal)
        vec_obj2_tangent = np.dot(v_obj2_tangent, v_unit_tangent)

        v_obj1_final = np.add(vec_obj1_normal, vec_obj1_tangent)
        v_obj2_final = np.add(vec_obj2_normal, vec_obj2_tangent)

        return Velocity(v_obj1_final[0], v_obj1_final[1]), Velocity(v_obj2_final[0], v_obj2_final[1])


def print_list(listOfObjects):
    for obj in listOfObjects:
        print "Position.x = %.5f Position.y = %.5f \n------------------" % (obj.position.x, obj.position.y)
    print "####"

deltaTime = 0.001
listOfObjects = []
for x in range(1,4):
    listOfObjects.append(BodyModel(Acceleration(x, x), Velocity(x, x), Position(x, x), x))

for x in range(10):
    listOfObjects = Physics.computeGravityInfluence(listOfObjects, deltaTime)
    printList(listOfObjects)

