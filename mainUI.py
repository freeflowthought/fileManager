import tkinter as tk
import json
from tkinter import messagebox
import os

from FindFiles import FindFilesWindow
from GetSize import GetSize
# ---------------------------- function field ------------------------------- #

# ---------------------------- search File Function ------------------------------- #




# ----------------------------Date Query Function------------------------------- #


# ---------------------------- Main Window Function ------------------------------- #

#create the makeCommandWindow function like MainWindow did for the rest of the class
class MainWindow:
    def __init__(self, parent) -> None:
        #The parent is the root=tk.TK()
        self.parent = parent
        # the childWindows is empty UI interface of the window.

        self.childWindows = []
         
        #childCommandInstances are the instantiation of the small widget and functions inside the childWindows
        self.childCommandInstances = []
        
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

        # Create buttons, #make findFilesButton to be the frame of the FindFilesWindow Class
        self.getSizeButton = tk.Button(
            self.frame,
            text='get Size',
            command=self.makeGetSize)
        #what does this line mean in here
        self.getSizeButton.pack(fill="both")


    def makeCommandWindow(self) -> tk.Toplevel:
        #this command returns a child window of a parent window, what toplevel does is to create a new window
        newWindow = tk.Toplevel(self.parent)
        self.childWindows.append(newWindow)
        return newWindow

    def makeFindFiles(self) -> None:
        #this command makes the the FindFilesWindow UI attached to the topLevel
        newParent = self.makeCommandWindow()
        newParent.title("FindFiles Function")
        self.childCommandInstances.append(FindFilesWindow(newParent))

    def makeGetSize(self) -> None:
         newParent = self.makeCommandWindow()
         newParent.title("Get Size Function")
         self.childCommandInstances.append(GetSize(newParent))


if __name__ == "__main__":
    #Global Config
    root = tk.Tk()
    #make root to be the parent of the main Window. root is an abstract concept which we don't see. but it's there for the MainWindow class
    window = MainWindow(root)
    root.mainloop()
