from tkinter import *
import json
from tkinter import messagebox
from utility import find_files
from datetime import datetime
import os
import time
from random import choice, randint, shuffle

# ---------------------------- CONSTANTS ------------------------------- #


# Next Action: fnameInput, fpathInput, and searchResult to be refactored as the global variables?


# ---------------------------- function field ------------------------------- #

# ---------------------------- Random String Generator------------------------------- #

#Password Generator Project
def generateRdstring():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    Rdletters = [choice(letters) for _ in range(randint(8, 10))]
    Rdsymbols = [choice(symbols) for _ in range(randint(2, 4))]
    Rdnumbers = [choice(numbers) for _ in range(randint(2, 4))]

    Rdlist = Rdletters + Rdsymbols + Rdnumbers
    shuffle(Rdlist)

    Rdstring = "".join(Rdlist)
    return Rdstring




# ---------------------------- search File Function ------------------------------- #


def searchFile():
    fnameInput = fileEntry.get()
    if "." not in fnameInput:
        messagebox.showinfo(
            title="File name input Error", message="Please include suffix in your search and make sure the search is not empty")
        fileEntry.delete(0, END)
        return
    fpathInput = pathEntry.get()
    if "\\" not in fpathInput:
        messagebox.showinfo(
            title="Path input error", message="Please contains the \ in your path input")
        pathEntry.delete(0, END)
        return
    #deal with the empty input. the tkinter has inserted an empty space before.  very nasty. there might be a better solution to resolve this bug.
    if len(text.get('1.0', END)) > 2:
        messagebox.showinfo(
            title="Result exists", message="Please clean your search result before an another search")
        text.delete('1.0', END)
        return


    searchResult = find_files(fnameInput, fpathInput)
    text.insert(END, f"{searchResult}")


# ---------------------------- Save Function------------------------------- #
def save():
    # date time properties needs to use the json.dumps to transfer to the json format(serialize)
    #this id needs to be as random as enough to serve as the identifier
    id = generateRdstring()
    
    fnameInput = fileEntry.get()
    fpathInput = pathEntry.get()
    searchResult = text.get('1.0', END)
    recordDate = json.dumps(datetime.now().strftime('%Y-%m-%d'))


    new_data = {
         id: {
            "fname": fnameInput,
            "pathname":  fpathInput,
            "searchResult":  searchResult,
            "recordDate":  recordDate,
        
        }
    }

    if len(fnameInput) == 0 or len(fpathInput) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    elif len(searchResult) < 3:
        messagebox.showinfo(title="Oops", message="your result doesn't look right. go check the input again")
    else:
        try:
            with open("json/searchFiles.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("json/searchFiles.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("json/searchFiles.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
             fileEntry.delete(0, END)
             pathEntry.delete(0, END)
             text.delete('1.0', END)
    

            

# ----------------------------Delete File Funtion------------------------------- #
def delete():
    try:
        os.remove("json/searchFiles.json")
    except FileNotFoundError:
        messagebox.showinfo(
            title="Oops", message="The File hasn't been created yet, you get nothing to delete")

# ----------------------------Date Query Function------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
#Global Config
window = Tk()
window.title("findFiles Function")
window.config(padx=35, pady=35)



# Labels
fileLabel = Label(window, text="File:")
fileLabel.grid(row=1, column=0)
pathLabel = Label(window, text="Path:")
pathLabel.grid(row=2, column=0)
textLabel = Label(window, text="Result:")
textLabel.grid(row=3, column=0)

# Entries
# fileEntry
fileEntry = Entry(width=40)
fileEntry.grid(row=1, column=1)
fileEntry.focus()
# path Entry
pathEntry = Entry(width=40)
pathEntry.grid(row=2, column=1)
pathEntry.focus()


# Buttons
search_button = Button(text="Search", width=9, command=searchFile)
#the first parameter for padx is left, the second parameter for pady is the right
search_button.grid(row=2, column=2,padx=(3,0))

#the tuple for pady, the first parameter for top, second parameter for buttom
add_button = Button(text="Save", width=30, command=save)
add_button.grid(row=4, column=1,pady=(5,5))

delete_button = Button(text="Delete", width=30, command=delete)
delete_button.grid(row=5, column=1,pady=(0,5))

# Todo This jumps to a new UI window to execute the Query function, there would be some command for switching the UI
query_button = Button(text="Date Query", width=30)
query_button.grid(row=6, column=1)


# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
text.grid(row=3, column=1)

window.mainloop()





