from tileSets import *

tileSet = tileSet3
newtiler = []

for tile in tileSet:

    if tile[1] != tile[2]:

        ntileH = tile[2]
        ntileW = tile[1]

        newtile = tile[0], ntileH, ntileW

        newtiler.append(tile)
        newtiler.append(newtile)
print newtiler
