__author__ = 'bartoszzasieczny'
from multiprocessing import Process
from time import sleep
import itertools

from core.physics.physics import *
from core.physics.body_model import *
#from core.communication_model import *

from server.server_events import *


class PhysicsProcess(Process):

    def __init__(self, config, publish_event_callback):
        Process.__init__(self)
        self.config = config
        self.publish = publish_event_callback
        self.objects = [[]]
        self.update_interval = 1.0/self.config.world.fps
        self.update_counter = 0
        self.ids_to_delete = set()
        self.is_running = False

    def init_objects(self):
        self.list_of_players = []
        self.list_of_planets=[]
        self.list_of_shots = []

        self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(100, 200), Force(0, 0), 1000, 25, "player"))
        self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(200, 300), Force(0, 0), 10, 25,"player"))
        #self.list_of_planets.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(300, 200), Force(0, 0), 10**13, 25))
        self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(600, 200), Force(1000, 0), 1000, 25,"player"))
        self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(500, 300), Force(-100, 50), 10, 25, "player"))
        #self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(300, 200), Force(50, 50), 1000, 25))
        #self.list_of_players.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(400, 300), Force(10, 10), 10, 25))

        self.list_of_planets.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(300, 200), Force(50, 50), 1000, 25, "planet"))
        self.list_of_planets.append(BodyModel(Acceleration(0, 0), Velocity(0, 0), Position(400, 300), Force(10, 10), 10, 25, "planet"))

        self.objects.append(self.list_of_players)
        self.objects.append(self.list_of_planets)
        self.objects.append(self.list_of_shots)


    def calculateFrame(self):
        self.ids_to_delete &= Physics.compute_gravity_influence(self.objects, self.update_interval)

        self.update_counter += 1

        if self.update_counter == self.config.world.update_interval:
            self.update_counter %= self.config.world.update_interval
            list_of_all_objects = list(itertools.chain.from_iterable(self.objects))
            self.send_objects_update(self.ids_to_delete, list_of_all_objects)
            self.ids_to_delete = set()

            # print "Object count: " + str(len(list_of_all_objects))
            # print "Positions:"
            # for obj in list_of_all_objects:
            #     print '%d: ' % obj.id, obj

        sleep(self.update_interval)

    def send_objects_update(self, ids_to_delete, all_objects):
        self.publish(UpdateEvent({
            "objects": all_objects,
            "ids_to_delete": ids_to_delete
        }))

    def run(self):
        self.init_objects()

        self.is_running = True
        while self.is_running:
            self.calculateFrame()


def physics_init(event_aggregator, config):

    physics_process = PhysicsProcess(config, event_aggregator.publish)

    # subscribe for events

    return physics_process
