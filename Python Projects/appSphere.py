import tkinter as tk
from tkinter import ttk

import Sphere as sp

class appSphere:
    def __init__ ( self, master):

        self.mas = master

        self.mas.title("appSphere")

        self.label1 = ttk.Label(self.mas, text = "Enter the sphere's radius:")
        self.label1.grid( row = 0, column = 0, pady = 10 )

        self.entry1 = ttk.Entry(self.mas, width = 10 )
        self.entry1.grid( row = 0, column = 1, pady = 10  )

        self.button1 = ttk.Button(self.mas, text="Calculate")
        self.button1.grid( row = 3, column = 0, pady = 10  )
        self.button1.config ( command = self.Calculate )

        self.button1 = ttk.Button(self.mas, text="Quit")
        self.button1.grid( row = 3, column = 2, pady = 10  )
        self.button1.config ( command = self.Exit )

        self.text1 = tk.Text( self.mas, height = 3, width = 40)
        self.text1.grid( row = 2, column = 0, columnspan = 3, pady = 10, padx = 10)

    def Calculate(self):
        string = self.entry1.get()
        radius = eval(string)
        s1 = sp.sphere(radius)
        self.text1.insert("1.0", f"Sphere with radius: = {s1} \n" )
        self.text1.insert("2.0", f"Volume = {s1.getVolume():.4f} \n" )
        self.text1.insert("3.0", f"SurfaceArea = {s1.getSurfaceArea():.4f}")

    def Exit(self):
        self.mas.destroy()


def main():
    win = tk.Tk()

    appT = appSphere(win)

    win.mainloop()


main()
