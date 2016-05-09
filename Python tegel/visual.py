#http://www.tutorialspoint.com/python/tk_canvas.htm
#http://zetcode.com/gui/tkinter/drawing/

import Tkinter
import tkMessageBox
from tegelset import *

#http://stackoverflow.com/questions/22950997/random-fill-colour-for-shapes-in-pythontkinter
import random

top = Tkinter.Tk()

print "coordinaten", placedCoordinates
print "tileset", tileSet
#alles keer 30?
C = Tkinter.Canvas(top, height=17*30, width=17*30)

X0list = []
Y1list = []
index = 0
colors = ["red", "orange", "yellow", "green", "blue", "violet"]

for tile in placedCoordinates:

    tileName = tile[0]
    X0 = tile[1]*30
    Y1 = tile[2]*30

    X0list.append(X0)
    Y1list.append(Y1)

    index += 1
    for tile2 in tileSet:

        if tileName == tile2[0]:

            print index
            if index > 1:
                Y0 = Y1list[index-1] + tile2[2]*30
                X1 = X0list[index-1] + tile2[1]*30

            else:
                Y0 = tile2[2]*30
                X1 = tile2[1]*30
            coor = X0, Y0, X1, Y1
            print coor
            tileName = C.create_rectangle(coor, fill= random.choice(colors), width=2)



C.pack()
top.mainloop()
