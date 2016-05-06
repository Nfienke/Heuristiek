from tileSets import *
"""
Importeren van een externe file:
MJJMeijerink,(2015).Heuristieken---Tegelzetten. Verkregen op 14, april, 2016 van https://github.com/MJJMeijerink/Heuristieken---Tegelzetten/tree/master/Source%20code%20files
"""
import sys
sys.setrecursionlimit(11000)
##http://stackoverflow.com/questions/31280555/python-recursive-algorithm-doesnt-work-for-large-values-c-program-works

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
            return False

        #checkt of...
        for x in range(tileWidth):
            if self.space[startY][startX + x] != 0:
                return False

        #plaatst de tegel.
        for i in range(tileHeight):
            for j in range (tileWidth):
                # als de tegel past wordt hij de tegel neergezet.
                self.space[startY + i][startX + j] = tileName

        # print canvas
        #self.visualizeCanvas()

        #Verwijdert de tegel uit de lijst van opties, als de tegel gebruikt is.
        tiles.sortTileSet.pop(tiles.index)

        #Roept functie aan om coordinaten per tegel op te slaan.
        coor = self.saveCoordinates(tileName, startX, startY)

        #begint met zoeken voor een tegel voor de volgende positie.
        return True

    def visualizeCanvas(self):

        for row in self.space:
            print row
        print '\n'


    def saveCoordinates(self, tileName, coorX, coorY):
        tiles = Tile

        coordinate = (tileName, coorX, coorY)
        tiles.Coordinates.append(coordinate)

        return tiles.Coordinates


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

    def removeTile(self):

        tiles = Tile
        lastIndex = 0

        #Zoekt de laast geplaatste tegel.
        for tile in tiles.Coordinates:
            lastIndex+=1
            lasttilepos = tile

        #verwijdert laatst gezsette tegel uit coordinaten:
        tiles.Coordinates.pop(lastIndex-1)


        #zoekt de laatste tegel op naam in tileset voor de afmetingen.
        for i in tileSet1:
            if i[0] == lasttilepos[0]:
                lasttile = i
        #afmetingen laastst geplaatste tegel.
        lasttileheight = lasttile[2]
        lasttilewidth = lasttile[1]
        #voegt tegel weer toe aan de Lijst sorttileset:
        tiles.sortTileSet.append((lasttilepos[0], lasttilewidth, lasttileheight))
        #opnieuw sorteren?
        tiles.sortTileSet = sorted(tiles.sortTileSet, key=lambda x: x[1],  reverse=True)
        print tiles.sortTileSet

        #tegel wordt verwijdert uit het canvas
        for i in range(lasttileheight):
            for j in range (lasttilewidth):
                # als de tegel past wordt hij de tegel neergezet.
                self.space[lasttilepos[2] + i][lasttilepos[1] + j] = 0

        # print canvas
        #self.visualizeCanvas()

        self.newTile(lasttilewidth)
        #dan mag je weer proberen maar niet die tegel zeg maar of met dezelfd afmetingen ...
        #return True

    def newTile(self, lasttilewidth):
        tiles = Tile
        canvas = Canvas
        index = 0
        #print "test"
        #print lasttilewidth

        for tile in tiles.sortTileSet:
            t = Tile(tile)

            if t.tileWidth != lasttilewidth:

                if canvas.placeTile(self, t.tileName, t.tileHeight, t.tileWidth):
                    self.runTileSetter()
                    ###

                    #terug naar vorige loop?!?hoe gaat hij dan weer normaal verder.?!
                    #####
                    return True

            index += 1

            if index == len(tiles.sortTileSet):
                #print "hier2"
                self.removeTile()
                return False

    def runTileSetter(self):

        tiles = Tile
        #canvas = Canvas

        #Loopt door de tiles set en....
        while tiles.sortTileSet:
            tiles.index = 0
            i = 0

            for tile in tiles.sortTileSet:
                #print tile
                #geeft elke tile eigenschappen
                t = Tile(tile)
                # zet tegel in canvas
                if self.placeTile(t.tileName, t.tileHeight, t.tileWidth):
                    break
                tiles.index += 1

                # als alle opties voor een positie niet kunnen dan stopt hij.
                if tiles.index == len(tiles.sortTileSet):
                    #print tiles.Coordinates

                    #remove laats gezette tegel??
                    self.removeTile()
                    return False



class Tile(object):
    """
    """
    def __init__(self, tile):

        self.tileHeight = tile[2]
        self.tileWidth = tile[1]
        self.tileName = tile[0]


    sortTileSet = sorted(tileSet1, key=lambda x: x[1],  reverse=True)
    #Lijst van coordinaten per tegel.
    Coordinates = []
    index = 0

def settingCanvas():

    canvas = Canvas(17,17)
    canvas.runTileSetter()


settingCanvas()
