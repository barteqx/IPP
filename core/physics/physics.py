# -*- coding: utf-8 -*-
from body_model import *
import math
import numpy as np
import itertools
__author__ = 'Pawel'


class Physics:
    shoots = 2
    constG = 6.67 * 10**-10
    force_resistance    = 100
    velocity_resistance = 30
    max_force    = 10**6
    max_velocity = 10**2 * 2

    def __init__(self):
        print Physics.constG
    #zakladam ze kazdy objekt bedzie mial informacje o swoim id, polozeniu, masie, aktualnej predkosci oraz pozycji
    #funkcja zwraca list� obiekt�w z zaktualizowanymi zmiennymi

    @staticmethod
    def compute_gravity_influence_for_one_list(list_of_objects, list_of_all_objects, delta_time, set_of_ids_to_delete):
        for obj in list_of_objects:
            force = Physics.__compute_force(list_of_all_objects, obj, delta_time)
            obj.acceleration = Physics.__compute_acceleration(force, obj.mass)
            obj.velocity = Physics.__compute_velocity(obj.velocity, obj.acceleration, delta_time, obj.type == "shoot")

            if obj.update_position(Physics.__compute_position(obj.position, obj.velocity, delta_time)) and obj.type == "shoot":
                set_of_ids_to_delete.add(obj.id)

    @staticmethod
    def compute_gravity_influence(list_of_lists, delta_time):
        #lista, w kotrej znajda sie zaktualizowane dane obiektow
        list_of_all_objects = list(itertools.chain.from_iterable(list_of_lists))
        set_of_ids_to_delete = set([])
        for obj in list_of_all_objects:
            Physics.__check_for_collision(obj, list_of_all_objects, set_of_ids_to_delete)
        for list_of_objects in list_of_lists:
            Physics.compute_gravity_influence_for_one_list(list_of_objects, list_of_all_objects, delta_time, set_of_ids_to_delete)

        for id in set_of_ids_to_delete:
            for l in list_of_lists:
                for obj in l:
                    if obj.id == id:
                        l.remove(obj)
        return set_of_ids_to_delete
        #for list_of_objects in list_of_lists:
        #    Physics.compute_gravity_influence_for_one_list(list_of_objects, list_of_all_objects, delta_time)


    @staticmethod
    def __compute_acceleration(force, mass):
        acceleration = Acceleration(0,0)
        if mass != 0:
            acceleration.x = force.x/mass
            acceleration.y = force.y/mass
        return acceleration

    @staticmethod
    def __compute_velocity(oldVelocity, acceleration, deltaTime, isShoot):
        velocity = Velocity(oldVelocity.x, oldVelocity.y)
        velocity.x += acceleration.x * deltaTime
        velocity.y += acceleration.y * deltaTime
        if isShoot:
            return velocity
        return Physics.__reduce_attribute(velocity, deltaTime, Physics.max_velocity, Physics.velocity_resistance)

    @staticmethod
    def __compute_position(oldPosition, velocity, deltaTime):

        position = Position(oldPosition.x, oldPosition.y)
        position.x += velocity.x * deltaTime
        position.y += velocity.y * deltaTime

        return position

    @staticmethod
    def __compute_force(listOfObjects, obj1, delta_time):
        force = obj1.force
        for obj2 in listOfObjects:
            r = math.sqrt((obj1.position.x - obj2.position.x)**2 + (obj1.position.y - obj2.position.y)**2)
            if r != 0:
                force.x += Physics.constG * obj1.mass * obj2.mass * math.fabs(obj1.position.x - obj2.position.x) / r**3
                force.y += Physics.constG * obj1.mass * obj2.mass * math.fabs(obj1.position.y - obj2.position.y) / r**3

        return Physics.__reduce_attribute(force, delta_time, Physics.max_force, Physics.force_resistance)
    @staticmethod
    def __reduce_attribute(attribute, delta_time, max, resistance):
        if attribute.x > 0:
            attribute.x -= resistance * delta_time

        if attribute.y > 0:
            attribute.y -= resistance * delta_time

        if attribute.x < 0:
            attribute.x += resistance * delta_time

        if attribute.y < 0:
            attribute.y += resistance * delta_time

        if attribute.x > max:
            attribute.x = max

        if attribute.y > max:
            attribute.y = max

        if attribute.x < -max:
            attribute.x = -max

        if attribute.y < -max:
            attribute.y = -max

        return attribute
    @staticmethod
    def __check_for_collision(obj, list_of_objects, set_of_ids_to_delete):
        for obj2 in list_of_objects:
            if obj.id is not obj2.id and Physics.__detect_collision(obj, obj2):
                #print("collision")
                if obj.type != "planet":
                    #print("shoot smth")
                    set_of_ids_to_delete.add(obj.id)
                    if obj2.type == "shoot":
                        set_of_ids_to_delete.add(obj2.id)
                        #print("shooted : %d" % obj2.id)
                else:
                    (v, v2) = Physics.__compute_velocities_at_collision(obj, obj2)
                    obj.velocity = v
                    obj2.velocity = v2
    @staticmethod
    def __detect_collision(obj1, obj2):

        if not (obj1.position and obj2.position):
            return False

        v_obj1 = np.array([obj1.position.x, obj1.position.y])
        v_obj2 = np.array([obj2.position.x, obj2.position.y])

        v_normal = np.array([v_obj1[0] - v_obj2[0], v_obj1[1] - v_obj2[1]])

        if np.linalg.norm(v_normal) <= (obj1.radius + obj2.radius):
            if np.linalg.norm(v_normal) < (obj1.radius + obj2.radius):
                obj1.position, obj2.position = obj1.last_position, obj2.last_position
            #print "collision detected, objects: %d and %d %s %s" % (obj1.id, obj2.id, obj1.type, obj2.type)
            #print v_normal
            return True

        else: return False

    @staticmethod
    def  __compute_velocities_at_collision(obj1, obj2):

        v_obj1 = np.array([obj1.velocity.x, obj1.velocity.y], dtype=np.float64)
        v_obj2 = np.array([obj2.velocity.x, obj2.velocity.y], dtype=np.float64)

        v_normal = np.array([v_obj1[0] - v_obj2[0], v_obj1[1] - v_obj2[1]])
        #print v_obj1, v_obj2
        #print v_normal

        if not np.linalg.norm(v_normal):
            #print "No colision..."
            return obj1.velocity, obj2.velocity

        v_unit_normal = np.divide(v_normal, np.linalg.norm(v_normal))
        v_unit_tangent = np.array([-1*v_unit_normal[1], v_unit_normal[0]])

        v_obj1_normal = np.vdot(v_unit_normal, v_obj1)
        v_obj1_tangent = np.vdot(v_unit_tangent, v_obj1)
        v_obj2_normal = np.vdot(v_unit_normal, v_obj2)
        v_obj2_tangent = np.vdot(v_unit_tangent, v_obj2)

        v_obj1_new_normal = (v_obj1_normal*(obj1.mass - obj2.mass) + 2*obj2.mass*v_obj2_normal)/(obj1.mass + obj2.mass)
        v_obj2_new_normal = (v_obj2_normal*(obj2.mass - obj1.mass) + 2*obj1.mass*v_obj1_normal)/(obj1.mass + obj2.mass)

        vec_obj1_normal = np.dot(v_obj1_new_normal, v_unit_normal)
        vec_obj1_tangent = np.dot(v_obj1_tangent, v_unit_tangent)
        vec_obj2_normal = np.dot(v_obj2_new_normal, v_unit_normal)
        vec_obj2_tangent = np.dot(v_obj2_tangent, v_unit_tangent)

        v_obj1_final = np.add(vec_obj1_normal, vec_obj1_tangent)
        v_obj2_final = np.add(vec_obj2_normal, vec_obj2_tangent)

        return Velocity(v_obj1_final[0], v_obj1_final[1]), Velocity(v_obj2_final[0], v_obj2_final[1])


