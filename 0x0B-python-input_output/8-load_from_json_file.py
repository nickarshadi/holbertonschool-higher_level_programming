#!/usr/bin/python3
""" JSON File decode Module. """
import json


def load_from_json_file(filename):
    """ load from json file. """
    with open(filename, 'r') as f:
        return json.load(f)
