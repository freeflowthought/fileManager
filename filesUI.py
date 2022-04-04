import tkinter as tk
import json
from tkinter import messagebox
from utility import find_files
from datetime import datetime, timezone
import os



# ---------------------------- function field ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #
#Global Config

class FindFilesWindow:
    currentSearchResult: list[str]

    def __init__(self, parent) -> None:
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
        self.query_button = tk.Button(self.frame, text="Date Query", width=30)
        self.query_button.grid(row=6, column=1)


         # Text
        self.currentSearchResult = None
        self.text = tk.Text(self.frame, height=5, width=30)
        self.text.grid(row=3, column=1)


    def searchFile(self):
        fnameInput = self.fileEntry.get()
        if "." not in fnameInput:
                messagebox.showinfo(
                    title="File name input Error", message="Please include suffix in your search and make sure the search is not empty")
                self.fileEntry.delete(0, tk.END)
                return
        fpathInput = self.pathEntry.get()
        if "\\" not in fpathInput:
                messagebox.showinfo(
                    title="Path input error", message="Please contains the \ in your path input")
                self.pathEntry.delete(0, tk.END)
                return
            #deal with the empty input. the tkinter has inserted an empty space before.  very nasty. there might be a better solution to resolve this bug.
        if len(self.text.get('1.0', tk.END)) > 2:
                messagebox.showinfo(
                    title="Result exists", message="Please clean your search result before an another search")
                self.text.delete('1.0', tk.END)
                return


        self.searchResult = find_files(fnameInput, fpathInput)
        self.text.insert(tk.END, self.searchResult)

    def save(self):
        #do the reading and writing at the same time and appending at the end of the line without truncating it.
        with open("json/searchFiles.json", "a+") as data_file:
            fileLength = data_file.tell()

            if fileLength:
                # There's data in the file. Read it
                data_file.seek(0)
                data = json.load(data_file)
                # Reset to start to prepare for write
                data_file.seek(0)
                #optimize the filesize
                data_file.truncate()
            else:
                data = {}
        
            # Updating old data with new data
            #process it to the standardized timezone
            data[datetime.now(timezone.utc).isoformat()] = {
                    "fname": self.fileEntry.get(),
                    "pathname":  self.pathEntry.get(),
                    "searchResult":  self.text.get('1.0', tk.END),
                }
        json.dump(data, data_file, indent=4)
        self.fileEntry.delete(0, tk.END)
        self.pathEntry.delete(0, tk.END)
        self.text.delete('1.0', tk.END)

    # ----------------------------Delete File Funtion------------------------------- #
    def delete(self):
        try:
            os.remove("json/searchFiles.json")
        except FileNotFoundError:
            messagebox.showinfo(
                title="Oops", message="The File hasn't been created yet, you get nothing to delete")


class MainWindow:
    def __init__(self,parent):
        self.parent = parent
        self.frame = tk.Frame(parent)
         #what does this line mean?
        self.frame.pack(fill="both")
        self.childWindow = []
        self.childInstance = []


        #create a findFileButton
        self.findFileaButton = tk.Button(self.frame,text='FindFiles',command=self.makeCommandWindow)
        self.findFileaButton.pack(fill="both")

    def makeCommandWindow(self) -> tk.Toplevel:
            #this command returns a child window of a parent window, what toplevel does is to create a new window
            newWindow = tk.Toplevel(self.parent)
            self.childWindow.append(newWindow)
            return newWindow
    
    def makeFindFiles(self) -> None:
        newParent = self.makeCommandWindow()
        newParent.title("FindFiles Function")
        self.childInstance.append(FindFilesWindow(newParent))



if __name__ == "__main__":
    root = tk.Tk()
    window = MainWindow(root)
    root.mainloop()