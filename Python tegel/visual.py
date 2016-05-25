"""
Opzet van een canvas visualisatie:
tutorialspoint,(2016).Python Tkinter Canvas. Verkregen op 9, mei, 2016 van http://www.tutorialspoint.com/python/tk_canvas.htm
"""

import Tkinter
import tkMessageBox
import random
from metdraaien import *

top = Tkinter.Tk()

#vergrotingsfactor
f = 20
canvas = Canvas
#creert scherm
C = Tkinter.Canvas(height=56*f, width=55*f)

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
            # kiest rgb's van verschillende tinten roze
            de=("%02x"%random.randint(255,255))
            re=("%02x"%random.randint(0,150))
            we=("%02x"%random.randint(120,200))
            ge="#"
            color=ge+de+re+we
            
            #geeft tegel kleur
            tileName = C.create_rectangle(coor, fill= color, width=1)
#tekent tegelset
C.pack()
top.mainloop()