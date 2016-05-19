from tilesets import *
"""
Importeren van een externe file:
MJJMeijerink,(2015).Heuristieken---Tegelzetten. Verkregen op 14, april, 2016 van https://github.com/MJJMeijerink/Heuristieken---Tegelzetten/tree/master/Source%20code%20files
"""

global tileSet
tileSet = []

global placedCoordinates
placedCoordinates = []

global sortTileSet
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

        # maak coordinaten door list van list te maken 2d-array/grid.
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
        self.visualizeCanvas()
        return True

    def saveCoordinates(self, tileName, coorX, coorY):
        """
        """
        coordinate = (tileName, coorX, coorY)
        placedCoordinates.append(coordinate)

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
        # gaat het  canvas af
        for i in range(self.heightCanvas):
            for j in range(self.widthCanvas):
                # zoek lege plek
                if self.space[i][j] == 0:
                    return (j,i)

    def visualizeCanvas(self):
        # ...
        for row in self.space:
            print row
        print '\n'


    def stepBack(self,stack, iStack, sortTileSet, tile):
        print "Ik kom in de StepBack", stack
        #Tegel zonder opties uit de stack verwijderen.
        stack.pop()

        print "tegel stepBack:", tile

        #appends tile to sorttileset again.
        if "*" in tile[0]:
            name = tile[0]
            name = name.replace("*","")
            tile = name, tile[2], tile[1]
            sortTileSet.append(tile)
        else:
            
            sortTileSet.append(tile)


        sortTileSet = sorted(sortTileSet , key=lambda x: x[1],  reverse=True)

        # Removes tile from the options left from his neighbour.
        print stack
       
        iStack = len(stack)
        print "hellup", tile, stack[iStack-1]
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
        checks whether there are options left for next to the placed tile,
        otherwise the placed tile needs to be removed.
        If there are options left it continues in runTileSetter.
        """
        print "nien", tile
        
        #if there are no options left for next to the placed tile.
        if len(stack[iStack][1]) < 1:
            
            tile = stack[iStack][0]
            print "nesxtstep if", tile, stack[iStack-1]
            return self.stepBack(stack, iStack, sortTileSet, tile)

        print "tgel nextStep", tile
        return stack, iStack, sortTileSet, tile

    def stackMaker(self, sortTileSet, stack, tile):
        """
        """
        #print "stackMaker: ", tile, sortTileSet
        stackTile = tile
        #removes tile from tileset
        options = []
        
        if "*" in tile[0]:
            
            name = tile[0]
            name = name.replace("*","")
            print name
            tile = name, tile[2], tile[1]
            sortTileSet.remove(tile)
        else:
            sortTileSet.remove(tile)
        
        

        #adds tile with options to the stack.
        # options = sortTileSet[:]

        for itile in sortTileSet:
            print itile
            if itile[1] != itile[2]:
                rotatedTile = itile[0]+"*", itile[2], itile[1]
                options.append(rotatedTile)
            options.append(itile)

        #creates a tuple, and adds this to the stack.
        value = (stackTile, options)
        stack.append(value)
        
        print "tegel stackMaker", tile
        return stack

    def runTileSetter(self):
        """
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

           
            stackMaker = self.stackMaker(sortTileSet, stack, tile)
           
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
            print "tegel runTileSetter", tile
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
                    name = tile[0]
                    name = name.replace("*","")
                    tile = name, tile[2], tile[1]
                    sortTileSet.append(tile)
                else:
                    sortTileSet.append(tile)

                sortTileSet = sorted(sortTileSet , key=lambda x: x[1],  reverse=True)

        print "hallo?", stack
        self.visualizeCanvas()

class Tile(object):
    """
    """
    def __init__(self, tile):

        self.tileHeight = tile[2]
        self.tileWidth = tile[1]
        self.tileName = tile[0]


def settingCanvas():

    canvas = Canvas(23,27)

    global tileSet
    tileSet = tileSet2

    canvas.runTileSetter()

settingCanvas()