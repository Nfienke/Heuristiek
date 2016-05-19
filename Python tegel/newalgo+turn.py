from tileSets import *
"""
Import from an online file:
MJJMeijerink,(2015).Heuristieken---Tegelzetten. Verkregen op 14, april, 2016 van https://github.com/MJJMeijerink/Heuristieken---Tegelzetten/tree/master/Source%20code%20files
"""

global tileSet
tileSet = []

global placedCoordinates
placedCoordinates = []

global sortTileSet
sortTileSet = sorted(tileSet , key=lambda x: x[1],  reverse=True)

global options
options = []


class Canvas():
    """
    The canvas represents the empty space
    that needs to be filled with the tiles.
    """

    def __init__ (self, width, height):
        """
        Creates the empty canvas
        """
        self.widthCanvas = width
        self.heightCanvas = height

        # Creates coordinates by making a list of a list in a 2d-array/grid.
        self.space = [[0 for count in range(width)] for count in range(height)]

    def placeTile(self, tileName, tileHeight, tileWidth):
        """
        Places a tile in the Canvas
        """
        # Find the next position of the tile
        start = self.findNextPosition()

        # Returns an x and an y coordinate to place a tile
        startX = start[0]
        startY = start[1]

        # Checks if the tile fits in the parameters of the Canvas
        if tileWidth + startX > self.widthCanvas or tileHeight + startY > self.heightCanvas:
            return False

        # Checks if the complete tile fits
        for x in range(tileWidth):
            if self.space[startY][startX + x] != 0:
                return False

        # If the tile fits, it is placed in the Canvas
        for i in range(tileHeight):
            for j in range (tileWidth):
                self.space[startY + i][startX + j] = tileName

        # Calls saveCoordinates to save every tile's coordinates
        coor = self.saveCoordinates(tileName, startX, startY)

        # Starts looking for tile for the next position
        self.visualizeCanvas()
        return True

    def saveCoordinates(self, tileName, coorX, coorY):
        """
        Saves the coordinates of all the placed tiles
        """
        coordinate = (tileName, coorX, coorY)
        placedCoordinates.append(coordinate)

        return placedCoordinates

    def findNextPosition(self):
        """
        Checks if the next tile fits next to the previous one, or a row below
        """
        # Goes through Canvas
        for i in range(self.heightCanvas):
            for j in range(self.widthCanvas):
                # Looks for empty spot
                if self.space[i][j] == 0:
                    return (j,i)

    def visualizeCanvas(self):
        """
        Prints the Canvas and the placed tiles (with a letter) and zeros for
        empty spots
        """
        for row in self.space:
            print row
        print '\n'


    def stepBack(self,stack, iStack, sortTileSet, tile):
        """
        Goes back in the tree to find the next branch of options
        """
        print "Ik kom in de StepBack", stack
        #Tegel zonder opties uit de stack verwijderen.
        stack.pop()

        #appends tile to sorttileset again.
        if "*" in tile[0]:
            tile[0] = tile[0].replace("*","")
            tile = tile[0], tile[2], tile[1]
            sortTileSet.append(tile)
        else:
            print "in de else", tile
            sortTileSet.append(tile)

        sortTileSet = sorted(sortTileSet , key=lambda x: x[1],  reverse=True)

        # Removes tile from the options left from his neighbour.
        stack[iStack-1][1].remove(tile)

        #als hele stack leeg is
        if iStack < 1:
            print "nienke error: not found", stack, sortTileSet
            quit()

        # Verwijdert tegel uit canvas en placedcoordinates.
        t = Tile(tile)
        #bepalen coordinate laatst geplaatste tegel.
        iCoor = len(placedCoordinates)-1
        lastTile = placedCoordinates[iCoor]
        placedCoordinates.remove(lastTile)

        #tegel wordt verwijdert uit het canvas
        for i in range(t.tileHeight):
            for j in range (t.tileWidth):
                self.space[lastTile[2] + i][lastTile[1] + j] = 0

        iStack = len(stack) - 1
        return self.nextStep(stack, iStack, sortTileSet, tile)

    def nextStep(self, stack, iStack, sortTileSet, tile):
        """
        Checks whether there are options left for next to the placed tile,
        otherwise the placed tile needs to be removed.
        If there are options left it continues in runTileSetter.
        """
        print "Ik zit in de nextStep"
        #if there are no options left for next to the placed tile.
        if len(stack[iStack][1]) < 1:
            tile = stack[iStack][0]
            print "De if statement van nextStep is gelukt"
            return self.stepBack(stack, iStack, sortTileSet, tile)

        return stack, iStack, sortTileSet, tile

    def stackMaker(self, sortTileSet, stack, tile):
        """
        Creates a stack with all the options for a next tile, including turned
        tiles
        """
        #print "stackMaker: ", tile, sortTileSet

        #removes tile from tileset
        print "help", tile, sortTileSet
        sortTileSet.remove(tile)

        stackTile = tile

        #adds tile with options to the stack.
        # options = sortTileSet[:]

        for tile in sortTileSet:
            if tile[1] != tile[2]:
                rotatedTile = tile[0]+"*", tile[2], tile[1]
                options.append(rotatedTile)
            options.append(tile)

        #creates a tuple, and adds this to the stack.
        value = (stackTile, options)
        stack.append(value)
        print "Ik ben door de if statement heen gegaan", stack

        return stack

    def runTileSetter(self):
        """
        Goes through the tree of options to see whether the tiles fit
        """
        stack = []
        iStack = 0

        sortTileSet = sorted(tileSet , key=lambda x: x[1],  reverse=True)

        while sortTileSet:
            #index for the stack
            iStack = len(stack)-1
            #search for a tile from the options of his neighbour,
            if len(stack) > 0:

                #returns the new values from the next step function,
                # for the values stack, iStack and sortTileSet.
                newValue = self.nextStep(stack, iStack, sortTileSet, tile)

                sortTileSet = newValue[2]
                #the tile is the first from the options of his neighbour.
                iStack = len(stack)-1
                tile = stack[iStack][1][0]

            #if the tile doesn't have a neighbour, then take the first from the sorttileset.
            else:
                tile = sortTileSet[0]

            #gets attributes from a tile.
            t = Tile(tile)

            print "voor de return", stack
            stackMaker = self.stackMaker(sortTileSet, stack, tile)
            print "SM", stackMaker
            print "na de return", stack

            # #removes tile from tileset.
            # sortTileSet.remove(tile)
            #
            # #adds tile with options to the stack.
            # options = sortTileSet[:]
            #
            # #creates a tuple, and adds this to the stack.
            # value = (tile, options)
            # stack.append(value)

            #checks if a tile fits in the placetile function.
            if self.placeTile(t.tileName, t.tileHeight, t.tileWidth):
                print "stack: ", stack
                continue

            #if a tile doesn't fit
            else:
                #removes tile with options from stack
                stack.pop()

                #removes tegel uit de opties van de tegel ervoor.
                iStack = len(stack)-1
                stack[iStack][1].remove(tile)

                #append to sortTileSet
                """
                Als je hem toevoegt, en het is een sterretje, dan moet je
                alleen de normale letter toevoegen
                """
                if "*" in tile[0]:
                    tile[0] = tile[0].replace("*","")
                    tile = tile[0], tile[2], tile[1]
                    sortTileSet.append(tile)
                else:
                    sortTileSet.append(tile)

                sortTileSet = sorted(sortTileSet , key=lambda x: x[1],  reverse=True)

        print "hallo?", stack
        self.visualizeCanvas()

class Tile(object):
    """
    Returns the parameters of a tile, as defined in tileSets.py
    """
    def __init__(self, tile):

        self.tileHeight = tile[2]
        self.tileWidth = tile[1]
        self.tileName = tile[0]


def settingCanvas():
    """
    Takes the parameters of the specific Canvas size and tileset
    """

    canvas = Canvas(23,27)

    global tileSet
    tileSet = tileSet2

    canvas.runTileSetter()

settingCanvas()
