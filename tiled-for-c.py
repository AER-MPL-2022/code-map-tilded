import sys
import json

class Map:
    def __init__(self, width, height, twidth, theight):
        self.size = (width, height)
        self.tile_size = (twidth,theight)
        self.layers = list()

class Layer:
    def __init__(self, width, height, data):
        self.size = (width, height)
        self.data = data

    def get_layer_data(self, f, map):
        for y in range(map.size[1]):
            for x in range(map.size[0]):
                if (self.data[y * map.size[0] + x] != 0):
                    #TODO: write x and y to file in the format "x y\n"

def get_map():
    filename = sys.argv[1]
    j = json.load(open(filename, "r"))
    #TODO: create map object
    for l in j["layers"]:
        #TODO: create layer object
        map.layers.append(layer)
    return map

    
map = get_map()
f = open("res.coll", "w")
for layer in map.layers:
    #TODO: if layer is collision layer then get layer data