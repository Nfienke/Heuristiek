from tileSets import *
"""
Importeren van een externe file:
MJJMeijerink,(2015).Heuristieken---Tegelzetten. Verkregen op 14, april, 2016 van https://github.com/MJJMeijerink/Heuristieken---Tegelzetten/tree/master/Source%20code%20files
"""
# ##http://stackoverflow.com/questions/31280555/python-recursive-algorithm-doesnt-work-for-large-values-c-program-works
import sys
sys.setrecursionlimit(11000)

#https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch04s09.html
from itertools import permutations
from itertools import *

global tileSet
tileSet = tileSet1

global placedCoordinates
placedCoordinates = []

global neighbourdict
neighbourdict = {}


sortTileSet = sorted(tileSet , key=lambda x: x[1],  reverse=True)



class Canvas():
    """
    The canvas represents the empty space
    that needs to be filled with the tiles.
    """

    def __init__ (self, width, height):
        """
        creates the empty canvas
        """
        self.widthCanvas = width
        self.heightCanvas = height

        # maak coordinaten door list van list te maken
        self.space = [[0 for count in range(width)] for count in range(height)]

    def placeTile(self, tileName, tileHeight, tileWidth):

        # zoek de volgende positie van de tegel
        start = self.findNextPosition()

        # geef x en y coordinaat om tegel neer te zetten
        startX = start[0]
        startY = start[1]

        # kijkt of de tegel wel binnen het canvas past.
        if tileWidth + startX > self.widthCanvas or tileHeight + startY > self.heightCanvas:
            return False
        #print"hello2"
        #checkt of de tegel er geheel in past.
        for x in range(tileWidth):
            if self.space[startY][startX + x] != 0:
                return False


        #plaatst de tegel indien het niet false is.
        for i in range(tileHeight):
            for j in range (tileWidth):
                # als de tegel past wordt hij de tegel neergezet.
                self.space[startY + i][startX + j] = tileName

        #Roept functie aan om coordinaten per tegel op te slaan.
        coor = self.saveCoordinates(tileName, startX, startY)

        #begint met zoeken voor een tegel voor de volgende positie.
        return True


    def saveCoordinates(self, tileName, coorX, coorY):


        coordinate = (tileName, coorX, coorY)
        #coordinateWidth = (tileName, coorX, coorY)
        placedCoordinates.append(coordinate)
        #tiles.allTriedCoordinates.append(coordinateWidth)


        return placedCoordinates


    def findNextPosition(self):
        """
        Fits the next tile next to the previous one?
        if yes
            placeTile
        else try next position  #eerst een stap naar rechts, als het canvas ophoudt, ga dan een rij omhoog
            if fits
                placeTile
            else
                go back to try next position
        """

        # ga de canvas af
        for i in range(self.heightCanvas):
            for j in range(self.widthCanvas):
                # zoek lege plek
                if self.space[i][j] == 0:
                    return (j,i)


    def runTileSetter(self):

        self.space = [[0 for count in range(17)] for count in range(17)]
        stack = []
        visited = []
        i = 0

        while sortTileSet:

            print "stack", stack
            print "tileset", sortTileSet
            print i
            tile = sortTileSet[i]
            print tile

            t = Tile(tile)

            options = sortTileSet[1:]
            value = (tile, options)
            stack.append(value)


            #print "lengte",len(stack)
            iStack = len(stack)-1

            if len(stack) > 1:
                #print "hello"
                #print "i", i
                #print "stak", tile, stack[iStack-1][1]
                if tile not in stack[iStack-1][1]:
                    stack.pop()
                    #print "not in?"

                    i += 1

                    #volgende proberen
                    continue


            if self.placeTile(t.tileName, t.tileHeight, t.tileWidth):

                #print tile, sortTileSet
                sortTileSet.remove(tile)
                #sorted(sortTileSet , key=lambda x: x[1],  reverse=True)
                #print sortTileSet
                i = 0

            else:

                stack.pop()
                #print"jo"
                #print iStack
                #print stack
                #print stack[iStack-1][1][0]
                stack[iStack-1][1].pop(0)
                #print"end"
                #print stack

                #quit()


        #
        # for tile in tileSet1:
        #     index += 1
        #     #print index
        #
        #     i = 0
        #
        #     for tile in newset:
        #         t = Tile(tile)
        #         positionTile = (t.tileName, i)
        #
        #         #print positionTile
        #
        #         if positionTile in forbidden:
        #             break
        #
        #
        #         # zet tegel in canvas
        #         if self.placeTile(t.tileName, t.tileHeight, t.tileWidth):
        #             i += 1
        #             continue
        #
        #         else:
        #
        #             forbidden.append(positionTile)
        #             #print forbidden
        #             skipNumbers = (len(newset)-(i+1))
        #
        #             self.updateloop(skipNumbers, index)
        #             break
                    #

class Tile(object):
    """
    """
    def __init__(self, tile):

        self.tileHeight = tile[2]
        self.tileWidth = tile[1]
        self.tileName = tile[0]


def settingCanvas():

    canvas = Canvas(17,17)
    #print sortTileSet

    forbidden = []

    canvas.runTileSetter()


settingCanvas()


def visualizeCanvas(self):
    # sort = sorted(tiles.allTriedCoordinates, key=lambda x: x[0],  reverse=False)
    # print "all", sort

    for row in self.space:
        print row
    print '\n'
    #print tiles.neighbourList
