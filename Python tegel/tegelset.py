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

    def stepBack(self,stack, iStack, sortTileSet):
        #print"ja"
        tile = stack[iStack][0]

        #lege optie uit stack halen
        stack.pop()


        #als hele stack leeg is
        if iStack < 1:
            print "not found", stack, sortTileSet
            quit()

        #removes tile from the options left from his neighbour.
        stack[iStack-1][1].remove(tile)

        iStack = iStack-1

        t = Tile(tile)

        #bepalen coordinate laatst geplaatste tegel.
        iCoor = len(placedCoordinates)-1
        lastTile =  placedCoordinates[iCoor]
        placedCoordinates.remove(lastTile)
        print lastTile
        #tegel wordt verwijdert uit het canvas
        for i in range(t.tileHeight):
            for j in range (t.tileWidth):
                self.space[lastTile[2] + i][lastTile[1] + j] = 0
        self.visualizeCanvas()

        if lastTile not in sortTileSet:
            #print "append1", tile
            sortTileSet.append(tile)
            sortTileSet = sorted(sortTileSet , key=lambda x: x[1],  reverse=True)
            #print sortTileSet

        self.nextStep(stack, iStack, sortTileSet)

    def nextStep(self, stack, iStack, sortTileSet):
        #print "ja2"
        #if there are no options left
        if len(stack[iStack][1]) < 1:

            tile = stack[iStack][0]
            #print "tegel is3:", tile
            #print "test2", tile
            #adds tile to the sorttileset again
            if tile not in sortTileSet:
                #print "append1", tile
                sortTileSet.append(tile)
                sortTileSet = sorted(sortTileSet , key=lambda x: x[1],  reverse=True)
                #print sortTileSet


            self.stepBack(stack, iStack, sortTileSet)

        else:

            return stack, iStack, sortTileSet

    def runTileSetter(self):

        self.space = [[0 for count in range(17)] for count in range(17)]
        stack = []
        i = 0
        iStack = 0
        sortTileSet = sorted(tileSet , key=lambda x: x[1],  reverse=True)


        while sortTileSet:
            #index for the stack
            iStack = len(stack)-1

            #search for a tile from the options of his neighbour,
            if len(stack) > 0:
                self.nextStep(stack, iStack, sortTileSet)
                #print"testing", len(stack), iStack
                iStack = len(stack)-1
                tile = stack[iStack][1][0]
                #sprint "tegel is2:", tile, stack
                #print "test", tile


            #if the tile doesn't have a neighbour, then take the first from the sorttileset.
            else:
                print "oeps"
                tile = sortTileSet[0]


            #gets attributes from a tile.
            t = Tile(tile)
            #print tile
            #print "tegel is:", tile

            #adds tile with options to the stack.
            options = sortTileSet[:]
            options = sorted(options , key=lambda x: x[1],  reverse=True)
            print options, tile, sortTileSet
            self.visualizeCanvas()
            options.remove(tile)


            value = (tile, options)
            stack.append(value)

            #print stack

            #print"1b", stack
            #checks if a tile fits.
            if self.placeTile(t.tileName, t.tileHeight, t.tileWidth):
                #print "remove", tile
                #if a tile fits, then remove tile from the sortTileSet.
                sortTileSet.remove(tile)
                #print sortTileSet

            #if a tile doesnt fit
            else:

                #removes last tile from stack
                stack.pop()

                #removes tile from the options left from his neighbour.

                #print len(stack)
                iStack = len(stack)-1
                #print stack[iStack][1]
                stack[iStack][1].remove(tile)
                #print "2", stack




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

    canvas.runTileSetter()


settingCanvas()
