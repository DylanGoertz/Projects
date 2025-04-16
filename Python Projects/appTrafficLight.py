import tkinter as tk
from tkinter import ttk

class appTrafficLight:

    def __init__ (self, master):

        self.mas = master

        self.width = 300
        self.height = 600
        self.can = tk.Canvas(self.mas, width = self.width,
                             height = self.height, bg="white")
        self.can.pack()

        self.text = self.can.create_text( 150, 50, text="click on one of the circles!", font=("Arial", 12))
        
        points1 = 75, 75, 200, 200
        self.oval1 = self.can.create_oval(points1, fill = "red", width = 1)

        points2 = 75, 225, 200, 350
        self.oval2 = self.can.create_oval(points2, fill = "yellow", width = 1)

        points3 = 75, 375, 200, 500
        self.oval3 = self.can.create_oval(points3, fill = "green", width = 1)

        self.can.bind("<ButtonPress-2>", self.mouse_press)

    def mouse_press(self, event):

        points1 = self.can.coords(self.oval1)
        points2 = self.can.coords(self.oval2)
        points3 = self.can.coords(self.oval3)

        if event > oval1:
            self.can.itemconfig(self.text, text="You clicked on red light")
        if event > oval2:
            self.can.itemconfig(self.text, text="You clicked on yellow light")
        if event > oval3:
            self.can.itemconfig(self.text, text="You clicked on green light")

        



def main():
    win = tk.Tk()
    appTraf = appTrafficLight(win)
    win.mainloop()

main()
