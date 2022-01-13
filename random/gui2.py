# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *
# from PIL import ImageTk,Image

# Creating master Tkinter window
# creates the main "widget" window
gui = Tk()
gui.geometry("400x400")
gui.title("Album Artwork Grabber GUI")

main_frame = LabelFrame(gui, text="Main Frame", width=500, height=500)
main_frame.pack()

top_frame = Label(
    main_frame, text="Welcome to the Album Artwork Scraper!")
top_frame.grid(row=0, column=0)

middle_frame = Label(
    main_frame, text="I'm the Middle Frame!")
middle_frame.grid(row=1, column=0)

bottom_frame = Label(
    main_frame, text="I'm the Bottom Frame!")
bottom_frame.grid(row=2, column=0)


# # Quit Button
# button_quit = Button(root, text="Exit Program", command=root.quit)
# button_quit.pack(side=BOTTOM)

gui.mainloop()


# # Creating master Tkinter window
# master = Tk()

# # Creating object of photoimage class
# # Image should be in the same folder
# # in which script is saved
# p1 = PhotoImage(
#     file='/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork/artwork.png')

# # Setting icon of master window
# master.iconphoto(False, p1)

# # Creating button
# b = Button(master, text='Click me !')
# b.pack(side=TOP)

# # Infinite loop can be terminated by
# # keyboard or mouse interrupt
# # or by any predefined function (destroy())
# mainloop()

# # from tkinter.ttk import *
# # from tkinter import *

# # Creating master Tkinter window
# root = Tk()
# root.title("Album Artwork Grabber GUI")

# p1 = PhotoImage(
#     file='/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork/artwork.png')

# # Setting icon of master window
# root.iconphoto(False, p1)

# root.mainloop()
