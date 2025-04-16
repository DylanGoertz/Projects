import tkinter as tk
from tkinter import ttk

class appFourCorner:

    def __init__ (self, master):

        self.mas = master
        
        self.width = 600
        self.height = 600
        self.can = tk.Canvas(self.mas, width = self.width,
                             height = self.height, bg ="black")
        self.can.pack()

        self.oval3_xspeed = 3
        points = 50, 550, 5, 595
        self.oval3 = self.can.create_oval(points, fill = "yellow", width = 10)

        self.oval1_yspeed = 3
        points = 5, 5, 50, 50
        self.oval1 = self.can.create_oval(points, fill = "red", width = 10)

        self.oval2_xspeed = 3
        points = 550, 5, 595, 50
        self.oval2 = self.can.create_oval(points, fill = "green", width = 10)

        points = 550, 550, 595, 595
        self.oval4_yspeed = 3
        self.oval4 = self.can.create_oval(points, fill = "blue", width = 10)

        self.can.after(30, self.moveObjects)

    def moveObjects(self):

                  # move ( object_shape, x_speed, y_speed )
        self.can.move(self.oval3, self.oval3_xspeed, 0 )
        self.can.move(self.oval1, self.oval1_yspeed, 0 )
        self.can.move(self.oval2, self.oval2_xspeed, 0 )
        self.can.move(self.oval4, self.oval4_yspeed, 0 )

        
        

                         # coords of object_shape
        x1, y1, x2, y2 = self.can.coords(self.oval3)
        a1, b1, a2, b2 = self.can.coords(self.oval1)
        c1, d1, c2, d2 = self.can.coords(self.oval2)
        e1, f1, e2, f2 = self.can.coords(self.oval4)

        if x2 > self.width:
            self.oval3_xspeed = -self.oval3_xspeed
        if x1 < 0:
            self.oval3_xspeed = -self.oval3_xspeed
        if b2 < 0:
            self.oval1_yspeed = -self.oval1_yspeed
        if b1 > self.height:
            self.oval1_yspeed = -self.oval1_yspeed
        if c2 > self.width:
            self.oval2_xspeed = -self.oval2_xspeed
        if c1 < 0:
            self.oval2_xspeed = -self.oval2_xspeed
        if f2 < 0:
            self.oval4_yspeed = -self.oval4_yspeed
        if f1 > self.height:
            self.oval4_yspeed = -self.oval4_yspeed


        self.can.after(30, self.moveObjects)






def main():
    win = tk.Tk()
    appFour = appFourCorner(win)
    win.mainloop()

main()
