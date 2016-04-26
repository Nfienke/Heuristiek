

from tileSets import *
"""
Importeren van een externe file:
MJJMeijerink,(2015).Heuristieken---Tegelzetten. Verkregen op 14, april, 2016 van https://github.com/MJJMeijerink/Heuristieken---Tegelzetten/tree/master/Source%20code%20files
"""

class Canvas():
    """
    The canvas represents the empty space
    that needs to be filled with the tiles.
    """

    def __init__ (self, width, height):
        """
        the
        """
        self.widthCanvas = width
        self.heightCanvas = height


        # maak coordinaten door list van list te maken

        self.space = [[0 for count in range(width)] for count in range(height)]

        #prints the canvas with freespace(0)
        # for row in self.space:
        #     print row
        #
        # print '\n'


    def placeTile(self, tileName, tileHeight, tileWidth):
        startX = 0
        startY = 0
        canvas = Canvas(17,17)


        for i in range(tileHeight):
            for j in range (tileWidth):
                if (canvas.space[startY + i][startX + j] == tileName):
                    return False

                canvas.space[startY + i][startX + j] = tileName

        for row in canvas.space:
            print row

        #updates position of tile in tile class

    def findNextPosition():
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

    def removeTile():
        print "leeg"

class Tile(object):
    """
    """
    def __init__(self, tile):

        self.tileHeight = tile[2]
        self.tileWidth = tile[1]
        self.tileName = tile[0]
        
        #aanroepen placetile functie
        canvas = Canvas(17,17)
        canvas.placeTile(self.tileName, self.tileHeight, self.tileWidth)
        #print self.tileName, self.tileWidth, self.tileHeight

    #begin positie van de tegel in Canvas.
    YPosition = []
    XPosition = []

def runTileSetter():

    #sorteren van groot naar klein.
    sortTileSet = sorted(tileSet1, key=lambda x: x[1],  reverse=True)

    #Loopt door de tileset.
    for tile in sortTileSet:
         Tile(tile)

runTileSetter()
