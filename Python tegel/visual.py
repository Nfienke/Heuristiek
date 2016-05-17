"""
Opzet van een canvas visualisatie:
tutorialspoint,(2016).Python Tkinter Canvas. Verkregen op 9, mei, 2016 van http://www.tutorialspoint.com/python/tk_canvas.htm
"""

import Tkinter
import tkMessageBox
import random
from tegelset import *

top = Tkinter.Tk()

#vergrotingsfactor
f = 30
#grootte van canvas keer de vergrotingsfactor.
C = Tkinter.Canvas(top, height=120*f, width=23*f)

#loopt door alle coordinaten van de geplaatste tegels voor het begin coordinaat,
#en voor elke tegel worden de coordinaten gegeven voor de rectangle.
for tile in placedCoordinates:

    tileName = tile[0]
    #X0 is het begin coordinaat X.
    X0 = tile[1]*f
    #Y0 is het begin coordinaat Y.
    Y1 = tile[2]*f

    #Ook moet voor elke tegel de afmetingen bekend zijn, verkregen uit tileSet.
    for tile2 in tileSet:

        if tileName == tile2[0]:

            #Y0 = Y1 + hoogte van de tegel,
            #en X1 = X0 + breedte van de tegel.
            Y0 = Y1 + tile2[2]*f
            X1 = X0 + tile2[1]*f

            """
            ZetCode,(2015).Drawing in Tkinter. Verkregen op 9, mei, 2016 van http://zetcode.com/gui/tkinter/drawing/
            """
            #Coordinaten van de rectangle(tegel).
            coor = X0, Y0, X1, Y1

            """
            Stackoverflow,(2014).Random fill colour for shapes in Python(TKinter). Verkregen op 9, mei, 2016 van http://stackoverflow.com/questions/22950997/random-fill-colour-for-shapes-in-pythontkinter
            """
            #tekent elke tegel in het canvas met een random color.
            tileName = C.create_rectangle(coor, fill= "#"+("%06x"%random.randint(0,16777215)), width=1)

C.pack()
top.mainloop()
