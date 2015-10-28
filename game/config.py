# -*- coding: utf-8 -*-

import json
from collections import namedtuple


class Config(object):

    __config_collection = {}

    @staticmethod
    def get(path_to_file):
        if path_to_file not in Config.__config_collection:
            Config.__config_collection[path_to_file] = Config.__load_config(path_to_file)
        return Config.__config_collection[path_to_file]

    @staticmethod
    def __load_config(path_to_file):
        stream = open(path_to_file)
        obj = json.load(stream)
        json_str = json.dumps(obj)
        return json.loads(json_str, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
