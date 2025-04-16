import tkinter as tk
from tkinter import ttk

class appCheckButton:

    def __init__ (self, master):

        self.mas = master
        self.mas.title("appCheckButton")
        self.mas.geometry("350x300")

        self.mas.rowconfigure(0, weight = 1)
        self.mas.rowconfigure(1, weight = 1)
        self.mas.rowconfigure(2, weight = 1)
        self.mas.columnconfigure(0, weight = 1)
        self.mas.columnconfigure(1, weight = 1)
        
        

        self.laf1 = tk.LabelFrame(self.mas, bd=0, text="", relief="ridge")
        self.laf1.grid(row = 0, column = 0,
                       sticky ="w", padx=0, pady = 0)

        self.label= ttk.Label(self.laf1, text="Pizza Joint",
                              font = ("Serif", 24, "italic"))
        self.label.pack()

        self.logo = tk.PhotoImage(file="pizza4.gif") # png, gif, ppm
        self.label.config( image = self.logo, compound = "right")
        self.small = self.logo.subsample(2,2)
        self.label.config( image = self.small)

        #######################################

        self.sham = tk.IntVar()
        self.flea = tk.IntVar()
        self.trim = tk.IntVar()
        self.shav = tk.IntVar()
        self.poop = tk.IntVar()
        self.help = tk.IntVar()

        self.laf2 = tk.LabelFrame(self.mas, bd=2, text="Toppings:",
                                  relief="ridge")
        self.laf2.grid(row = 2, column = 0, sticky="we", padx = 5)

        self.check1 = tk.Checkbutton(self.laf2, text="Mushrooms", width = 10,
                                     height = 1, anchor="w")
        self.check1.grid(row =0, column = 0)
        
        self.check2 = tk.Checkbutton(self.laf2, text="Hot Peppers", width = 10,
                                     height = 1, anchor="w")
        self.check2.grid(row =0, column = 1)

        self.check3 = tk.Checkbutton(self.laf2, text="Pepperoni", width = 10,
                                     height = 1, anchor ="w")
        self.check3.grid(row =1, column = 0)

        self.check4 = tk.Checkbutton(self.laf2, text="Onions", width = 10,
                                     height = 1, anchor="w")
        self.check4.grid(row =1, column = 1)

        self.check1.config( variable = self.sham, offvalue = 0, onvalue = 1)
        self.check2.config( variable = self.flea, offvalue = 0, onvalue = 1)
        self.check3.config( variable = self.trim, offvalue = 0, onvalue = 1)
        self.check4.config( variable = self.shav, offvalue = 0, onvalue = 1)

        checks = [self.check1, self.check2, self.check3, self.check4]
        for c in checks:
            c.config( command = self.cal )
        

        ########################################

        self.laf3 = tk.LabelFrame(self.mas, bd=2, text="Pizza Size:", relief="ridge",
                                  width = 300, height = 20)
        self.laf3.grid(row = 1, column = 0, sticky="we", padx = 5)

        self.check1 = tk.Checkbutton(self.laf3, text="Regular", width = 10,
                                     height = 1, anchor="w")
        self.check1.grid(row =0, column = 0)
        
        self.check2 = tk.Checkbutton(self.laf3, text="Large", width = 10,
                                     height = 1, anchor="w")
        self.check2.grid(row =0, column = 1)

        self.check1.config( variable = self.poop, offvalue = 0, onvalue = 1 )
        self.check2.config( variable = self.help, offvalue = 0, onvalue = 1 )

        checks = [self.check1, self.check2]
        for c in checks:
            c.config( command = self.cal )
        
        #####################################

        self.laf4 = tk.LabelFrame(self.mas, bd=2, text="", relief="ridge",
                                  width = 275, height = 2)
        self.laf4.grid(row = 3, column = 0, sticky="w")

        self.text = tk.Text(self.laf4, width = 300, height = 1)
        self.text.pack(anchor="w")

        #####################################

    def cal(self):
        self.text.delete("1.0", "end")
        total = 0
        if self.help.get() == 1:
            total += 10.00
        if self.poop.get() == 1:
            total += 7.00
        if self.sham.get() == 1:
            total = total + .75
        if self.flea.get() == 1:
            total += .85
        if self.trim.get() == 1:
            total += 1.25
        if self.shav.get() == 1:
            total += .75
        self.text.insert("1.0", f"${total:.2f}")

    def clear(self):
        self.text.delete("1.0", "end")
        self.sham.set(0)
        self.flea.set(0)
        self.trim.set(0)
        self.shav.set(0)
        self.poop.set(0)
        self.help.set(0)

    def done(self):
        self.mas.destroy()

        



def main():
    win = tk.Tk()
    appCheck = appCheckButton(win)
    win.mainloop()
main()
