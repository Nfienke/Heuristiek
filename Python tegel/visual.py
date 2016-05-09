#http://www.tutorialspoint.com/python/tk_canvas.htm
#http://zetcode.com/gui/tkinter/drawing/

import Tkinter
import tkMessageBox
from tegelset import *
top = Tkinter.Tk()

print "coordinaten", placedCoordinates
print "tileset", tileSet
#alles keer 20?
C = Tkinter.Canvas(top, height=340, width=340)
X0list = []
Y1list = []
index = 0
for tile in placedCoordinates:
    tileName = tile[0]
    X0 = tile[1]*20
    Y1 = tile[2]*20
    X0list.append(X0)
    Y1list.append(Y1)
    #print tile[0]
    index += 1
    for tile2 in tileSet:
        #print tile2[0]



        if tileName == tile2[0]:

            print index
            if index > 1:
                Y0 = Y1list[index-1] + tile2[2]*20
                X1 = X0list[index-1] + tile2[1]*20

            else:
                Y0 = tile2[2]*20
                X1 = tile2[1]*20
            coor = X0, Y0, X1, Y1
            print coor
            tileName = C.create_rectangle(coor, fill="blue", width=2)



C.pack()
top.mainloop()
