import tkinter as tk
import json
from tkinter import messagebox
import os
from spawnUI import SpawnsChildWindows
from FindFiles import FindFilesWindow
from GetSize import GetSize
from unzip import UnzipCopy
# ---------------------------- function field ------------------------------- #

# ---------------------------- search File Function ------------------------------- #




# ----------------------------Date Query Function------------------------------- #


# ---------------------------- Main Window Function ------------------------------- #

#create the makeCommandWindow function like MainWindow did for the rest of the class
class MainWindow(SpawnsChildWindows):
    def __init__(self, parent) -> None:
        #The parent is the root=tk.TK()
        super().__init__(parent)
         
       
        
        # Create a root object for the rest of the items
        #make MaiWindow to be the parent of the FindFields Window and the rest of the windows which need to be created
        self.frame = tk.Frame(parent)

        #what does this line mean?
        self.frame.pack(fill="both")

        # Create buttons, #make findFilesButton to be the frame of the FindFilesWindow Class
        self.findFilesButton = tk.Button(
            self.frame,
            text='Find Files',
            command=self.makeFindFiles)
        #what does this line mean in here
        self.findFilesButton.pack(fill="both")

        # Create buttons, #make getSizeButton to be the frame of the GetSize Class
        self.getSizeButton = tk.Button(
            self.frame,
            text='get Size', pady=20,
            command=self.makeGetSize)
        #what does this line mean in here
        self.getSizeButton.pack(fill="both")


        self.unzipButton = tk.Button(self.frame, text="unzip function",command=self.makeUnzip)
        self.unzipButton.pack(fill="both")


    def makeFindFiles(self) -> None:
        #this command makes the the FindFilesWindow UI attached to the topLevel
        #it was being inherited by spawnUI class
         self.initializeCommandWindow("FindFile Function", FindFilesWindow)

    def makeGetSize(self) -> None:
         
         self.initializeCommandWindow("GetSize Function",GetSize)

    def makeUnzip(self) -> None:
    
        self.initializeCommandWindow("UnzipCopy Function",UnzipCopy)


if __name__ == "__main__":
    #Global Config
    root = tk.Tk()
    #make root to be the parent of the main Window. root is an abstract concept which we don't see. but it's there for the MainWindow class
    window = MainWindow(root)
    root.mainloop()
