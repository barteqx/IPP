from body_model import *
import math
__author__ = 'Pawel'


class Physics:
    constG = 6.67 * 10**-11

    def __init__(self):
        print Physics.constG
    #zakladam ze kazdy objekt bedzie mial informacje o swoim id, polozeniu, masie, aktualnej predkosci oraz pozycji
    #funkcja zwraca listê obiektów z zaktualizowanymi zmiennymi
    @staticmethod
    def computeGravityInfluence(listOfObjects, deltaTime):
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
    def __computeAcceleration(force, mass):
        acceleration = Acceleration(0,0)
        if mass != 0:
            acceleration.x = force.x/mass
            acceleration.y = force.y/mass

        return acceleration

    @staticmethod
    def __computeVelocity(oldVelocity, acceleration, deltaTime):
        velocity = Velocity(oldVelocity.x, oldVelocity.y)
        velocity.x += acceleration.x * deltaTime
        velocity.y += acceleration.y * deltaTime

        return velocity

    @staticmethod
    def __computePosition(oldPosition, velocity, deltaTime):
        position = Position(oldPosition.x, oldPosition.y)
        position.x += velocity.x * deltaTime
        position.y += velocity.y * deltaTime

        return position

    @staticmethod
    def __computeForce(listOfObjects, obj1):
        force = Force(0,0)
        for obj2 in listOfObjects:
            r = math.sqrt((obj1.position.x - obj2.position.x)**2 + (obj1.position.y - obj2.position.y)**2)
            if r != 0:
                force.x += Physics.constG * obj1.mass * obj2.mass * (obj1.position.x - obj2.position.x) / r**3
                force.y += Physics.constG * obj1.mass * obj2.mass * (obj1.position.y - obj2.position.y) / r**3

        return force


def printList(listOfObjects):
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

