from tilesets import *
    """
    Importeren van een externe file:
    MJJMeijerink,(2015).Heuristieken---Tegelzetten. Verkregen op 14, april, 2016 van https://github.com/MJJMeijerink/Heuristieken---Tegelzetten/tree/master/Source%20code%20files
    """

class Canvas(object):
    """
    The canvas represents the empty space
    that needs to be filled with the tiles.
    """

    def __init__ (self, width, height):
        """
        the
        """
        # maak coordinaten door list van list te maken
        space = [[0 for count in range(width)] for count in range(height)]

        #prints the canvas with freespace(0)
        for row in space:
            print row
        print '\n'
       

        # proto om tegels te zetten
        tileWidth = 5
        tileHeight = 5
        for i in range(tileHeight):
            for j in range (tileWidth):
                space[i][j] = 1
        
        for row in space:
            print row

    
        



x = Canvas(10,10)



class Tileset:
    """
    """

    def Tile(self, width, height, name):
        """
        Width, height
        """

    # Sorteren groot naar klein.
    sortTileSet = []

    #for i in sortTileSet:
        #past ie?

    
