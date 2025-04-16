import tkinter as tk
from tkinter import ttk

class appRadioButton:

    def __init__(self, master):

        self.mas = master

        self.mas.geometry("250x150")

        self.mas.title("appRadioButton")

        self.label_frame1 = tk.LabelFrame(self.mas, text="", bd = 0,
                                         relief ="ridge", height = 200, width = 350)
        self.label_frame1.pack(anchor="w", fill="x", padx = 5, pady = 5)

        self.label1 = ttk.Label(self.label_frame1, text="1st number:")
        self.label1.grid( row = 0 , column = 0 )

        self.entry1 = ttk.Entry(self.label_frame1, width="10")
        self.entry1.grid( row = 0, column = 1 )

        self.label2 = ttk.Label(self.label_frame1, text="2nd number:")
        self.label2.grid( row = 1 , column = 0 )

        self.entry2 = ttk.Entry(self.label_frame1, width="10")
        self.entry2.grid( row = 1, column = 1 )

        

        ################################################

        self.label_frame2 = tk.LabelFrame(self.mas, text="Select an Operator", bd = 2,
                                         relief ="ridge", height = 200, width = 350)
        self.label_frame2.pack(anchor="w", fill="x", padx = 5, pady = 5)

        self.greet = tk.StringVar()
        self.greet.set(None)

        radio1 = tk.Radiobutton(self.label_frame2, text="+", variable = self.greet,
                                value="+" )

        radio2 = tk.Radiobutton(self.label_frame2, text="-", variable = self.greet,
                                value="-" )
        
        radio3 = tk.Radiobutton(self.label_frame2, text="*", variable = self.greet,
                                value="*" )

        radio4 = tk.Radiobutton(self.label_frame2, text="/", variable = self.greet,
                                value="/" )


        radios =[radio1, radio2, radio3, radio4]

        for r in radios:
            r.pack(side="left")

        for r in radios:
            r.config ( command = self.select)

        ################################################


        self.label_frame3 = tk.LabelFrame(self.mas, text="", bd = 0,
                                         relief ="ridge", height = 200, width = 350)
        self.label_frame3.pack(anchor="w", fill="x", padx = 5, pady = 5)

        self.label = ttk.Label(self.label_frame3, text="", font=("Serif", 24, "bold"))
        self.label.pack()
        

        #################################################

    def select(self):
        string1 = self.entry1.get()
        x1 = eval(string1)
        string2 = self.entry2.get()
        x2 = eval(string2)
        if self.greet.get() == "+":
            self.label.config(text = f"{x1 + x2}")
        if self.greet.get() == "-":
            self.label.config(text = f"{x1 - x2}")
        if self.greet.get() == "*":
            self.label.config(text = f"{x1 * x2}")
        if self.greet.get() == "/":
            self.label.config(text = f"{x1 / x2}")
        




def main():
    win = tk.Tk()
    appRad = appRadioButton(win)
    win.mainloop()

main()
