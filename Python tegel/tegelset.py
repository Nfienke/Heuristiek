from tilesets import *
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

    def placeTile(self, tileName, tileHeight, tileWidth):
        # zoek de volgende positie
        start = self.findNextPosition()
        
        # geef x en y coordinaat om tegel neer te zetten
        startX = start[0]
        startY = start[1]

        # ga af of de tegel past op elke coordinaat 
        for i in range(tileHeight):
            for j in range (tileWidth):
                if self.space[startY + i][startX + j] != 0 or tileWidth + startX > self.widthCanvas or tileHeight + startY > self.heightCanvas:
                    print "past niet"
                    return False

                # zet tegel neer
                self.space[startY + i][startX + j] = tileName
                 

        # print canvas
        for row in self.space:
            print row
        print '\n'

        #updates position of tile in tile class

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
        #self.canvas = Canvas(17,17)
        
        #print self.tileName, self.tileWidth, self.tileHeight

    #begin positie van de tegel in Canvas.
    YPosition = []
    XPosition = []

def runTileSetter():

    #sorteren van groot naar klein.
    sortTileSet = sorted(tileSet1, key=lambda x: x[1],  reverse=True)

    canvas = Canvas(17,17)
    #Loopt door de tileset.
    for tile in sortTileSet:
        #geeft elke tile eigenschappen
        t = Tile(tile)
        # zet tegel in canvas
        canvas.placeTile(t.tileName, t.tileHeight, t.tileWidth)

runTileSetter()