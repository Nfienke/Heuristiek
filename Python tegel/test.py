from tileSets import *

tileSet = tileSet3
newtiler = []

for tile in tileSet:

    if tile[1] != tile[2]:

        newtile = tile[0], tile[2], tile[1]

        newtiler.append(tile)
        newtiler.append(newtile)
