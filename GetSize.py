import tkinter as tk
from tkinter import messagebox
from utility import getSize
from Decoration import on_enter,on_leave

class GetSize:
    def __init__(self,parent) -> None:
        self.frame = tk.Frame(parent,padx=30,pady=35)
        self.frame.pack(side="top")


        #input area
        self.pathLabel = tk.Label(self.frame, text="path:")
        self.pathLabel.grid(row=1, column=0)
        #Entry
        self.pathEntry = tk.Entry(self.frame, width=40)
        self.pathEntry.grid(row=1, column=1)
        self.pathEntry.focus()

        self.textLabel = tk.Label(self.frame, text="Result:")
        self.textLabel.grid(row=3, column=0)


        #need a button
         # Buttons
        self.get_button = tk.Button(self.frame, text="Find", width=9,command=self.getFile)
        #the first parameter for padx is left, the second parameter for pady is the right
        self.get_button.grid(row=2, column=1,padx=(3,0))


        #need a text area
        self.getSizeResult = None
        self.text = tk.Text(self.frame, height=5, width=30)
        self.text.grid(row=3, column=1)

    #get function
    def getFile(self) -> None:
        pathInput = self.pathEntry.get()
        self.getSizeResult = getSize(pathInput)
        self.text.insert(tk.END, self.getSizeResult)





