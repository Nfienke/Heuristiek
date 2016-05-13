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

        #self.visualizeCanvas()

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

    def visualizeCanvas(self):
        # sort = sorted(tiles.allTriedCoordinates, key=lambda x: x[0],  reverse=False)
        # print "all", sort

        for row in self.space:
            print row
        print '\n'
        #print tiles.neighbourList




    def runTileSetter(self):

        self.space = [[0 for count in range(17)] for count in range(17)]
        stack = []
        i = 0
        iStack = 0

        while sortTileSet:
            #index for the stack
            iStack = len(stack)-1

            #search for a tile from the options of his neighbour,
            if len(stack) > 0:

                #if there are no options left
                if len(stack[iStack][1]) < 1:
                    print"no left"
                    tile = stack[iStack][0]
                    print tile
                    #removes tile with no options left
                    stack.pop()
                    print stack

                    #adds tile to the sorttileset again
                    if tile not in sortTileSet:

                        sortTileSet.append(tile)
                        sorted(sortTileSet , key=lambda x: x[1],  reverse=True)

                    #removes tile from the options left from his neighbour.
                    stack[iStack-1][1].pop(0)
                    #rint stack[iStack-1][1]


                    iStack = iStack - 1

                    #if neighbour is also  out of options.
                    if len(stack[iStack][1]) < 1:
                        print stack
                        tile = stack[iStack][0]
                        print tile
                        #removes tile with no options left
                        stack.pop()
                        print stack

                        #adds tile to the sorttileset again
                        if tile not in sortTileSet:

                            sortTileSet.append(tile)
                            sorted(sortTileSet , key=lambda x: x[1],  reverse=True)

                        #removes tile from the options left from his neighbour.
                        stack[iStack-1][1].pop(0)
                        #rint stack[iStack-1][1]


                        iStack = len(stack)
                        tile = stack[iStack-1][1][0]
                        print stack
                        

                else:

                    tile = stack[iStack][1][0]

            #if the tile doesn't have a neighbour, then take the first from the sorttileset.
            else:

                tile = sortTileSet[0]

            print tile

            #gets attributes from a tile.
            t = Tile(tile)

            #adds tile with options to the stack.
            options = sortTileSet[:]
            options.remove(tile)
            value = (tile, options)
            stack.append(value)

            print stack

            #checks if a tile fits.
            if self.placeTile(t.tileName, t.tileHeight, t.tileWidth):

                #if a tile fits, then remove tile from the sortTileSet.
                sortTileSet.remove(tile)


            else:
                print "false"
                #removes last tile from stack
                stack.pop()
                print "test"

                #adds tile to the sorttileset again
                if tile not in sortTileSet:

                    sortTileSet.append(tile)
                    sorted(sortTileSet , key=lambda x: x[1],  reverse=True)

                #removes tile from the options left from his neighbour.
                # print stack[iStack][1][0]
                print "hey"

                stack[iStack][1].pop(0)

                print stack



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
