from tileSets import *
"""
Importeren van een externe file:
MJJMeijerink,(2015).Heuristieken---Tegelzetten. Verkregen op 14, april, 2016 van https://github.com/MJJMeijerink/Heuristieken---Tegelzetten/tree/master/Source%20code%20files
"""
import sys
sys.setrecursionlimit(14900)
# ##http://stackoverflow.com/questions/31280555/python-recursive-algorithm-doesnt-work-for-large-values-c-program-works

global tileSet
tileSet = tileSet2

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
        tiles = Tile
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

        #coortile = (tileName, startX, startY)
        # if coortile in tiles.allTriedCoordinates:
        #     return False

        neighbour2 = []
        for tile in tiles.placedCoordinates:

            neighbour2.append(tile[0])

        neighbour2.append(tileName)

        if neighbour2 in tiles.neighbourList:
            return False

        #plaatst de tegel indien het niet false is.
        for i in range(tileHeight):
            for j in range (tileWidth):
                # als de tegel past wordt hij de tegel neergezet.
                self.space[startY + i][startX + j] = tileName

        #Verwijdert de tegel uit de lijst van opties, als de tegel gebruikt is.
        tiles.sortTileSet.pop(tiles.index)

        # print canvas
        #self.visualizeCanvas()



        #Roept functie aan om coordinaten per tegel op te slaan.
        coor = self.saveCoordinates(tileName, startX, startY)

        #begint met zoeken voor een tegel voor de volgende positie.
        return True

    def visualizeCanvas(self):
        tiles = Tile
        # sort = sorted(tiles.allTriedCoordinates, key=lambda x: x[0],  reverse=False)
        # print "all", sort

        for row in self.space:
            print row
        print '\n'
        #print tiles.neighbourList

    def saveCoordinates(self, tileName, coorX, coorY):
        tiles = Tile

        coordinate = (tileName, coorX, coorY)
        #coordinateWidth = (tileName, coorX, coorY)
        tiles.placedCoordinates.append(coordinate)
        #tiles.allTriedCoordinates.append(coordinateWidth)


        neighbour = []
        neighbourindex = len(tiles.placedCoordinates)
        if neighbourindex > 0:
            for tile in tiles.placedCoordinates:

                neighbour.append(tile[0])


            tiles.neighbourList.append(neighbour)

        return tiles.placedCoordinates, tiles.neighbourList #, tiles.allTriedCoordinates


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
        """
        zoekt de laatst geplaatste tegel en verwijdert deze uit het canvas
        en voegt hem toe aan de lijst met mogelijk tegels(sorttileset)
        """

        tiles = Tile
        global lasttile
        lindex = 0

        #Zoekt de laast geplaatste tegel.
        for tile in tiles.placedCoordinates:
            lindex += 1
            lasttilepos = tile

        if lasttilepos[1] == 0 and lasttilepos[2] == 0:
            print "niet eerste weghalen"
            print "laatst geplaatste tegel", lasttilepos
            print "tiles.placedCoordinates:", tiles.placedCoordinates
            quit()

        tiles.placedCoordinates.pop(lindex -1)

        #zoekt de laatste tegel op naam in tileset voor de afmetingen.
        for i in  tileSet :
            if i[0] == lasttilepos[0]:
                lasttile = i
        #print "lasttile", lasttile
        #afmetingen laastst geplaatste tegel.
        lasttileheight = lasttile[2]
        lasttilewidth = lasttile[1]
        #voegt tegel weer toe aan de Lijst sorttileset:

        tiles.sortTileSet.append((lasttilepos[0], lasttilewidth, lasttileheight))
        #opnieuw sorteren
        tiles.sortTileSet = sorted(tiles.sortTileSet, key=lambda x: x[1],  reverse=True)


        #tegel wordt verwijdert uit het canvas
        for i in range(lasttileheight):
            for j in range (lasttilewidth):
                self.space[lasttilepos[2] + i][lasttilepos[1] + j] = 0

        # print canvas
        #self.visualizeCanvas()

        #self.newTile(lasttilewidth)
        #dan mag je weer proberen maar niet die tegel zeg maar of met dezelfd afmetingen ...
        self.runTileSetter()


    # moeten checken ook op tile breedte welke al op die positie is geweest om het efficienter te maken.
    #         if t.tileWidth != lasttilewidth:


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
        self.visualizeCanvas()



class Tile(object):
    """
    """
    def __init__(self, tile):

        self.tileHeight = tile[2]
        self.tileWidth = tile[1]
        self.tileName = tile[0]


    sortTileSet = sorted(tileSet , key=lambda x: x[1],  reverse=True)
    #Lijst van coordinaten per tegel.
    placedCoordinates = []
    #
    allTriedCoordinates = []
    #
    neighbourList = []

    index = 0

def settingCanvas():

    canvas = Canvas(23,27)

    canvas.runTileSetter()


settingCanvas()
    #
    # def runSimulation(speed, width, height, tiles), num_trials:
    #     """
    #     Runs NUM_TRIALS trials of the simulation and returns the mean number of
    #     time-steps needed to clean the fraction MIN_COVERAGE of the room.
    #
    #     speed: a float (speed > 0)
    #     width: an int (width > 0)
    #     height: an int (height > 0)
    #
    #     num_trials: an int (num_trials > 0)
    #
    #     """
    #     anim = visualisationTegelzetten(tileSet, width, height)
    #     num = num_trials
    #     totaltime = 0
    #
    #     while num > 0:
    #         room = RectangularRoom(width, height)
    #         coor = []
    #         anim.update(room, coor)
    #         while tileSet niet leeg is
    #             for tile in tiles:
    #                 Canvas.placeTile
    #                 anim.update(room, coor)
    #             totaltime += 1
    #         anim.update(room, coor)
    #     return float(totaltime/num_trials)
    #
    #     anim.done()
