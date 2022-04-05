import tkinter as tk
from tkinter import messagebox
import json
from utility import find_files
from datetime import datetime, timezone
import os



# ---------------------------- Save Function------------------------------- #
def saveToJson(fname: str, pathname: str, searchResult: list[str]) -> None:
    # This function is not included in the FindFilesWindow class for a good reason
    # That reason is to try and isolate code to one responsibility
    # The FindFilesWindow class is responsible for interacting with the user and checking whether input is valid
    # This function is responsible for performing the actual action itself and takes arguments it knows are already valid

    with open("json/searchFiles.json", "a+") as data_file:
        fileLength = data_file.tell()

        if fileLength:
            # There's data in the file. Read it
            data_file.seek(0)
            data = json.load(data_file)
            # Reset to start to prepare for write
            data_file.seek(0)
            data_file.truncate()
        else:
            data = {}
    
        # Updating old data with new data
        data[datetime.now(timezone.utc).isoformat()] = {
                "fname": fname,
                "pathname":  pathname,
                "searchResult":  searchResult
            }
        json.dump(data, data_file, indent=4)



class FindFilesWindow:
    currentSearchResult: list[str]

    def __init__(self, parent) -> None:
        # the childWindows is empty UI interface of the window.
        self.parent = parent
        self.childWindows = []
         
        #childCommandInstances are the instantiation of the small widget and functions inside the childWindows
        self.childCommandInstances = []
        self.frame = tk.Frame(parent, padx=35, pady=35)
        self.frame.pack(side="top")
        # Create interface

        # Labels
        self.fileLabel = tk.Label(self.frame, text="File:")
        self.fileLabel.grid(row=1, column=0)
        self.pathLabel = tk.Label(self.frame, text="Path:")
        self.pathLabel.grid(row=2, column=0)
        self.textLabel = tk.Label(self.frame, text="Result:")
        self.textLabel.grid(row=3, column=0)

        # Entries
        # fileEntry
        self.fileEntry = tk.Entry(self.frame, width=40)
        self.fileEntry.grid(row=1, column=1)
        self.fileEntry.focus()
        # path Entry
        self.pathEntry = tk.Entry(self.frame, width=40)
        self.pathEntry.grid(row=2, column=1)
        self.pathEntry.focus()


        # Buttons
        self.search_button = tk.Button(self.frame, text="Search", width=9, command=self.searchFile)
        #the first parameter for padx is left, the second parameter for pady is the right
        self.search_button.grid(row=2, column=2,padx=(3,0))

        #the tuple for pady, the first parameter for top, second parameter for buttom
        self.add_button = tk.Button(self.frame, text="Save", width=30, command=self.save)
        self.add_button.grid(row=4, column=1,pady=(5,5))

        self.delete_button = tk.Button(self.frame, text="Delete", width=30, command=self.delete)
        self.delete_button.grid(row=5, column=1,pady=(0,5))

        # Todo This jumps to a new UI window to execute the Query function, there would be some command for switching the UI
        self.query_button = tk.Button(self.frame, text="Date Query", width=30,command=self.makeQuery)
        self.query_button.grid(row=6, column=1)
 

        # Text
        self.currentSearchResult = None
        self.text = tk.Text(self.frame, height=5, width=30)
        self.text.grid(row=3, column=1)

    def searchFile(self) -> None:
        fnameInput = self.fileEntry.get()
        fpathInput = self.pathEntry.get()
        self.currentSearchResult = find_files(fnameInput, fpathInput)
        self.text.insert(tk.END, self.currentSearchResult)
    
    def save(self) -> None:
        # DO INPUT VALIDATION HERE
        if self.currentSearchResult is None:
            messagebox.showinfo(title="Oops", message="Need to search before saving")
            # Exit early
            return
        
        fnameInput = self.fileEntry.get()
        fpathInput = self.pathEntry.get()

        saveToJson(fnameInput, fpathInput, self.currentSearchResult)

        # Clear the inputs
        self.fileEntry.delete(0, tk.END)
        self.pathEntry.delete(0, tk.END)
        self.text.delete("1.0", tk.END)
        self.currentSearchResult = None

 # ----------------------------Delete File Funtion------------------------------- #
    
    def delete(self) -> None:
        try:
            os.remove("json/searchFiles.json")
        except FileNotFoundError:
            messagebox.showinfo(
            title="Oops", message="The File hasn't been created yet, nothing to delete")

    def makeCommandWindow(self) -> tk.Toplevel:
        #this command returns a child window of a parent window, what toplevel does is to create a new window
        #this line of the code has the problem
        newWindow = tk.Toplevel(self.parent)
        self.childWindows.append(newWindow)
        return newWindow

    def makeQuery(self) -> None:
        newParent = self.makeCommandWindow()
        newParent.title("Query Result")
        self.childCommandInstances.append(QueryWindow(newParent))



class QueryWindow:

    def __init__(self, parent) -> None:
        # the childWindows is empty UI interface of the window.
        self.frame = tk.Frame(parent, padx=30, pady=25)
        self.frame.pack(side="top")
        # Create interface

        self.textLabel = tk.Label(self.frame, text="Result:")
        self.textLabel.grid(row=1, column=0)

        self.text = tk.Text(self.frame, height=5, width=30)
        self.text.grid(row=2, column=0)

    

