import tkinter as tk
from tkinter import messagebox
from utility import copyUnzip,_copy,_unzip
from Decoration import on_enter,on_leave


class UnzipCopy:
    def __init__(self,parent) -> None:
        self.frame = tk.Frame(parent,padx=30,pady=35)
        self.frame.pack(side="top")

        #source input label
        self.sourceLabel = tk.Label(self.frame, text="source file:")
        self.sourceLabel.grid(row=1, column=0)

        #source input Entry
        self.sourceEntry = tk.Entry(self.frame, width=40)
        self.sourceEntry.grid(row=1, column=1)
        
        #dest input label
        self.destLabel = tk.Label(self.frame,text="dest path:")
        self.destLabel.grid(row=2,column=0)

        #dest input Entry
        self.destEntry = tk.Entry(self.frame, width=40)
        self.destEntry.grid(row=2,column=1)

        #button entry -- waiting to add the unzip method here
        self.unzipButton = tk.Button(self.frame,text="Unzip", width=9,command=self.unzip)
        self.unzipButton.bind("<Enter>", on_enter)
        self.unzipButton.bind("<Leave>", on_leave)

        self.unzipButton.grid(row=3,column=1,columnspan=2)

    def unzip(self) -> None:
        srcInput = self.sourceEntry.get()
        destInput = self.destEntry.get()
        #or not have the return
        return copyUnzip(srcInput,destInput)




        
