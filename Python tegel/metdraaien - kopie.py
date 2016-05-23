from tileSets import *
"""
Importeren van een externe file:
MJJMeijerink,(2015).Heuristieken---Tegelzetten. Verkregen op 14, april, 2016 van https://github.com/MJJMeijerink/Heuristieken---Tegelzetten/tree/master/Source%20code%20files
"""

#initeert tegelset
global tileSet
tileSet = []

#onthoud geplaatste tegels met coordinaten
global placedCoordinates
placedCoordinates = []

#gesoortde set van tegels groot>klein
global sortTileSet
sortTileSet = sorted(tileSet , key=lambda x: x[1],  reverse=True)

# maakt counter om aantal stappen te tellen
global counter
counter = 0


class Canvas():
    """
    Canvas geeft de ruimte waar de tegels worden geplaatst weer
    in de vorm van 2d array
    """

    def __init__ (self, width, height):
        """
       creert leeg canvas
       geeft hoogte en breedte meer
        """

        self.widthCanvas = width
        self.heightCanvas = height

        # maak coordinaten door list van list te maken 2d-array/grid.
        self.space = [[0 for count in range(width)] for count in range(height)]

    
    def placeTile(self, tileName, tileHeight, tileWidth):

        # zoek de volgende positie van de tegel, dmv nestPosition
        start = self.findNextPosition()

        # geeft x en y coordinaat om tegel neer te zetten
        startX = start[0]
        startY = start[1]

        # kijkt of de tegel wel binnen het canvas past.
        if tileWidth + startX > self.widthCanvas or tileHeight + startY > self.heightCanvas:
            return False

        #checkt of de tegel niet overlapt met andere tegels.
        for x in range(tileWidth):
            
            if self.space[startY][startX + x] != 0:
                return False

        #plaatst de tegel indien het niet false is.
        for i in range(tileHeight):
            
            for j in range (tileWidth):
                
                # verandert coordinaten in tileName
                self.space[startY + i][startX + j] = tileName

        #Roept functie aan om coordinaten per tegel op te slaan.
        coor = self.saveCoordinates(tileName, startX, startY)

        #roept counter op
        global counter
        #telt bij elke geplaatste tegel 
        counter += 1
        
        # tegelgeplaatse terug naar run tileSetter        
        return True

    
    def saveCoordinates(self, tileName, coorX, coorY):
        """
        stopt plaats en naam van tegel in tuple
        en plaats tuple in global list placedCoordinates
        """
        coordinate = (tileName, coorX, coorY)
        placedCoordinates.append(coordinate)

        return placedCoordinates


    
    def findNextPosition(self):
        """
        gaat de 2d array af en zoekt naar de eerst volgende lege plek
        """
        # gaat het  canvas af
        for i in range(self.heightCanvas):
            
            for j in range(self.widthCanvas):
                
                # zoek lege plek
                if self.space[i][j] == 0:
                    #return coordinaten
                    return (j,i)

    
    def visualizeCanvas(self):
        #tekent 2d array
        for row in self.space:
            print row
        print '\n'


    
    def stepBack(self,stack, iStack, sortTileSet, tile):
        """
        als er geen mogelijkheid is om de volgende tegel te plaatsen
        verwijder huidige tegel
        """
        #laatst geplaatste tegel uit de stack verwijderen.
        stack.pop()
        #onthoudt tegel
        stacktile = tile
       
        #checkt of tegel gekanteld is
        if "*" in tile[0]:
            name = tile[0]
            #past tilename aan
            name = name.replace("*","")
            tile = name, tile[2], tile[1]
            # stopt tegel terug in sortTileSet
            sortTileSet.append(tile)
        else:
            #stopt tegel terug in sortTileSet
            sortTileSet.append(tile)
        
        #sorteer tegelset weer    
        sortTileSet = sorted(sortTileSet , key=lambda x: x[1],  reverse=True)

        # check met index van stack groote van stack.
        iStack = len(stack)

        #verwijder tegel van stack
        stack[iStack-1][1].remove(stacktile)

        #checkt of iStack leeg is ofwel zijn alle opties geprobeerd
        if iStack < 1:
            print "nienke error: not found", stack, sortTileSet
            quit()

        # Verwijdert tegel uit canvas en placedcoordinates.
        t = Tile(stacktile)
        
        #bepalen coordinate laatst geplaatste tegel.
        iCoor = len(placedCoordinates)-1
        lastTile = placedCoordinates[iCoor]
        placedCoordinates.remove(lastTile)

        #tegel wordt verwijdert uit het canvas
        for i in range(t.tileHeight):
            for j in range (t.tileWidth):
                self.space[lastTile[2] + i][lastTile[1] + j] = 0

        #update index van stack
        iStack = len(stack) - 1

        return self.nextStep(stack, iStack, sortTileSet, tile)

    
    def nextStep(self, stack, iStack, sortTileSet, tile):
        """
        Checkt wat de volgende tegel is om te zetten
        """
        
        #checkt of er nog opties zijn om volgende tegel te plaatsen
        if len(stack[iStack][1]) < 1:

            # zo nee, pakt eerste tegel uit de opties
            tile = stack[iStack][0]
            # en roep stepBack aan met laatst geplaatste tegel
            return self.stepBack(stack, iStack, sortTileSet, tile)


        # anders ga door in RunTileSetter
        return stack, iStack, sortTileSet, tile

    
    def stackMaker(self, sortTileSet, stack, tile):
        """
        stackMaker plaats tegel in de stack met opties volgende tegels
        """
        
        # gebruike huidige tegel
        stackTile = tile
        
        #initeert opties
        options = []

        # checkt of tegel gekantelt is
        if "*" in tile[0]:

            name = tile[0]
            #wijzig tileName
            name = name.replace("*","")
            tile = name, tile[2], tile[1]
            #verwijder tegel uit sortTileSet
            sortTileSet.remove(tile)
        else:
            #doe dit ook als tegel niet gekanteld is
            sortTileSet.remove(tile)

        # ga elke tegel in sortTileSet af
        for itile in sortTileSet:
            # als tegel niet vierkant is..
            if itile[1] != itile[2]:
                # zet geroteerde tegel ook in opties
                rotatedTile = itile[0] + "*", itile[2], itile[1]
                options.append(rotatedTile)
            # zet tegel in opties
            options.append(itile)

        #maakt tuple van tegel en volgende tegels.
        value = (stackTile, options)
        stack.append(value)

        return stack

    def runTileSetter(self):
        """
        loopt door sortTileSet heen en zoekt de volgorde van plaatsen van tegels
        """
        #leeg stack
        stack = []
        # zet index op nul
        iStack = 0

        # roep sortTileSet aan
        sortTileSet = sorted(tileSet , key=lambda x: x[1],  reverse=True)

        # zolang er nog tegels in sortTileSet zitten
        while sortTileSet:
            #index voor de stack
            iStack = len(stack)-1
            #als er opties zijn voor de volgende tegele,
            if len(stack) > 0:

                # update de stack sortTileSet en tegels,
                newValue = self.nextStep(stack, iStack, sortTileSet, tile)

                sortTileSet = newValue[2]
                # pak eerste tegel van de opties
                iStack = len(stack)-1
                tile = stack[iStack][1][0]

            # als er nog geen tegels geplaatst zijn zet de eerste tegel neer
            else:
                tile = sortTileSet[0]

            #geef kenmerken door van de tegel.
            t = Tile(tile)

            # roep stackMaker aan
            stackMaker = self.stackMaker(sortTileSet, stack, tile)

           
            #roept placeTile aan
            if self.placeTile(t.tileName, t.tileHeight, t.tileWidth):
                # als het past, continue
                continue

            #als de tegel niet past
            else:
                #verwijder tegel met opties van de stack
                stack.pop()

                #verwijder tegel uit de opties van de tegel ervoor.
                iStack = len(stack)-1
                stack[iStack][1].remove(tile)

                """
                Als je hem toevoegt, en er is een sterretje in de naam, dan moet je
                alleen de normale letter toevoegen
                """
                if "*" in tile[0]:
                    name = tile[0]
                    name = name.replace("*","")
                    tile = name, tile[2], tile[1]
                    sortTileSet.append(tile)
                else:
                    #append aan sortTileSet
                    sortTileSet.append(tile)

                # sorteer de sortTileSet
                sortTileSet = sorted(sortTileSet , key=lambda x: x[1],  reverse=True)

        # roep visualizeCanvas aan en prin counter
        self.visualizeCanvas()
        print counter



class Tile(object):
    """
    geeft naam en lengte en breedte mee aan tegel
    """
    def __init__(self, tile):

        self.tileHeight = tile[2]
        self.tileWidth = tile[1]
        self.tileName = tile[0]

def settingCanvas():
    """
    zet instellingen voor verschillende sets
    """
    global tileSet
    # tileSet1
    canvas = Canvas(17,17)
    tileSet = tileSet1

    #tileSet2
    #canvas = Canvas(23,27)
    #tileSet = tileSet2

    #tileSet3
    #canvas = Canvas(55,56)
    #tileSet = tileSet3

    #roep runTileSetter aan
    canvas.runTileSetter()
# zet de code aan
settingCanvas()