from tileSets import *
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
        space = []
        row=[]
        for i in range(0,width):

            row.append(0)
            for i in range(0, height):
                space.append(row)

        #prints the canvas with freespace(0)
        for row in space:
            print row

x = Canvas(17,17)



class Tileset:
    """
    """

    # Sorteren groot naar klein.
    sortTileSet = []

    #for i in sortTileSet:
        #past ie?

    def Tile(self, width, height, name):
        """
        Width, height
        """
