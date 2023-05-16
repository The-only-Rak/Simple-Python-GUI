import tkinter as tkk
import numpy as np
from math import *
pointers = np.array([0, 0, 0, 1, 1, 1, 1, 0]) * 50
k = 2
degree = -90
zp = [200, 200]

class Window(tkk.Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.frame1 = tkk.Frame()
        self.frame2 = tkk.Frame()
        self.label1 = tkk.Label(text="K")
        self.canvas = tkk.Canvas(bg="white", width=800, height=600)
        def cp(event):
            global zp
            zp[0] = event.x
            zp[1] = event.y
            draw(self.canvas)
        self.canvas.bind("<Button-1>",cp)
        def mu(*args):
            global k
            k += 0.1
            draw(self.canvas)
        def md(*args):
            global k
            k -= 0.1
            draw(self.canvas)
        self.bm1, self.bm2 = tkk.Button(
            self.frame1, text="<", command=md), tkk.Button(self.frame1, text=">", command=mu)
        self.bind("<Key-Left>",md)
        self.bind("<Key-Right>",mu)
        self.bm1.grid(row=0, column=0)
        self.bm2.grid(row=0, column=1)
        self.label2 = tkk.Label(text="Degree")

        def du(*args):
            global degree
            degree += 5
            draw(self.canvas)

        def dd(*args):
            global degree
            degree -= 5
            draw(self.canvas)

        self.bd1, self.bd2 = tkk.Button(
            self.frame2, text="<", command=dd), tkk.Button(self.frame2, text=">", command=du)
        self.bind("<Control-Left>",du)
        self.bind("<Control-Right>",dd)
        self.bd1.grid(row=0, column=0)
        self.bd2.grid(row=0, column=1)
        self.canvas.pack()
        self.label1.pack()
        self.frame1.pack()
        self.label2.pack()
        self.frame2.pack()
        draw(self.canvas)


def draw(cnv: tkk.Canvas):
    global pointers
    cnv.delete("all")
    r1 = np.array([[k, 0], [0, k]])
    r2 = np.array([[cos(radians(degree)), sin(radians(degree))],
                   [-sin(radians(degree)), cos(radians(degree))]])
    res = []
    for i, j in np.split(pointers, len(pointers) / 2):
        tmp = np.array([i, j])
        tmp = np.matmul(tmp, r1)
        tmp = np.matmul(tmp, r2)
        tmp = tmp + zp
        res.extend(tmp)
    cnv.create_polygon(*res)
    cnv.update()


win:Window = Window()
win.title("Lab 9")
win.mainloop()