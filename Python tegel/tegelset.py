

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
        space = [[0 for count in range(width)] for count in range(height)]

        #prints the canvas with freespace(0)
        for row in space:
            print row
        print '\n'


    def placeTile(tileHeight, tileWidth):
        startX = 3
        startY = 3

        for i in range(tileHeight):
            for j in range (tileWidth):
                if (space[startY + i][startX + j] == 1):
                    return False

                space[startY + i][startX + j] = 1

        for row in space:
            print row

        #updates position of tile in tile class
    #print space # waarom kent ie space niet?
    placeTile(2,2)

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

        #hoe roep je dit dan aan? eerste tile plaatsen,placetile
        #canvas.placeTile(self.tileHeight, self.tileWidth)

        #print self.tileName, self.tileWidth, self.tileHeight


    #begin positie van de tegel in Canvas.
    YPosition = []
    XPosition = []






def runTileSetter():

    canvas = Canvas(17,17)

    #sorteren van groot naar klein.
    sortTileSet = sorted(tileSet1, key=lambda x: x[1],  reverse=True)

    #
    for tile in sortTileSet:
         Tile(tile)





runTileSetter()
