###### THIS IS A SAMPLE GUI ######

# Make a generally nice-looking GUI for the user (welcome screen, etc.).
# Have the GUI ask the user to direct the application to the folder where their music files live.
# Somehow store the music location as a value to use in the artwork grabber scripts themselves

### Features to include ###

# General welcome text
# Dynamic progress bar as artwork is found and added...?
# Logo?
# Asks the user for where their music library is/what file(s) they want artwork added to.
#

# https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/

# EVERYTHING is a WIDGET in Tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# creates the main "widget" window
gui = Tk()
gui.geometry("400x400")
gui.title("Album Artwork Grabber")

# creates a reusable class that contains all the properties and functions for selecting a folder


class FolderSelect(Frame):
    def __init__(self, parent=None, folderDescription="", **kw):
        Frame.__init__(self, master=parent, **kw)
        self.folderPath = StringVar()  # automatically updates fields
        self.lblName = Label(self, text=folderDescription)
        self.lblName.grid(row=0, column=0)
        self.entPath = Entry(self, textvariable=self.folderPath)
        self.entPath.grid(row=0, column=1)
        self.btnFind = ttk.Button(
            self, text="Browse Folder", command=self.setFolderPath)
        self.btnFind.grid(row=0, column=2)

    def setFolderPath(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)

    @property
    def folder_path(self):
        return self.folderPath.get()


def doStuff():
    folder1 = directory1Select.folder_path
    folder2 = directory2Select.folder_path
    print("Doing stuff with folder", folder1, folder2)


folderPath = StringVar()

directory1Select = FolderSelect(gui, "Select your music library")
directory1Select.grid(row=0)

directory2Select = FolderSelect(
    gui, "Select where you want album artwork stored")
directory2Select.grid(row=1)

c = ttk.Button(gui, text="find", command=doStuff)
c.grid(row=4, column=0)
gui.mainloop()


# https: // stackoverflow.com/questions/51877124/how-to-select-a-directory-and-store-it-into-a-variable-in-tkinter/51877299
