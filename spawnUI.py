import tkinter as tk
from Decoration import on_enter,on_leave



class SpawnsChildWindows:
    '''The purpose of this UI is to separate the common logic for the code reuse, it will be inherited by its child class with super'''

    #return type
    childWindows: list[tk.Toplevel]

    def __init__(self,parent) -> None:
        self.parent = parent
        self.childWindows = []
         #childCommandInstances are the instantiation of the small widget and functions inside the childWindows
        self.childCommandInstances = []
        self.frame = tk.Frame(parent)

    def makeCommandWindow(self) -> tk.Toplevel:
        newWindow = tk.Toplevel(self.parent)
        self.childWindows.append(newWindow)
        return newWindow

    def initializeCommandWindow(self, title: str, commandClass):
        newParent = self.makeCommandWindow()
        newParent.title(title)
        self.childCommandInstances.append(commandClass(newParent))


