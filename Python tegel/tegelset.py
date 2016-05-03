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
        creates the canvas
        """
        self.widthCanvas = width
        self.heightCanvas = height

        # maak coordinaten door list van list te maken
        self.space = [[0 for count in range(width)] for count in range(height)]

    def placeTile(self, tileName, tileHeight, tileWidth):
        tiles = Tile
        # zoek de volgende positie van de tegel
        start = self.findNextPosition()

        # geef x en y coordinaat om tegel neer te zetten
        startX = start[0]
        startY = start[1]

        # ga af of de tegel past op elke coordinaat
        
        if tileWidth + startX > self.widthCanvas or tileHeight + startY > self.heightCanvas:
            print "past niet"
            return False
              
        for x in range(tileWidth):
            if self.space[startY][startX + x] != 0:
                print "past ook niet"
                return False
                   
                
        for i in range(tileHeight):
            for j in range (tileWidth):            
                # als de tegel past wordt hij de tegel neergezet.
                self.space[startY + i][startX + j] = tileName



        #verwijder de tegel uit de lijst met opties
        #loop weer door de lijst met tegels van groot naar klein.
        # print canvas (aparte functie worden --> visualize canvas).
        for row in self.space:
            print row
        print '\n'
        tiles.sortTileSet.pop(tiles.index)
        print tiles.sortTileSet
        return True

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


    sortTileSet = sorted(tileSet1, key=lambda x: x[1],  reverse=True)

    index = 0

    #begin positie van de tegel in Canvas.
    YPosition = []
    XPosition = []

def runTileSetter():

    tiles = Tile

    #print tiles.sortTileSet

    canvas = Canvas(17,17)
    #Loopt door de tileset.

    while tiles.sortTileSet:
        tiles.index = 0
        for tile in tiles.sortTileSet:
            print tile
            #geeft elke tile eigenschappen
            t = Tile(tile)
            # zet tegel in canvas
            if canvas.placeTile(t.tileName, t.tileHeight, t.tileWidth):
                break
            tiles.index += 1

runTileSetter()