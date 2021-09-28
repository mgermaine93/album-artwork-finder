###### THIS IS A SAMPLE GUI ######
# https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/

# EVERYTHING is a WIDGET in Tkinter
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# creates the main "window" widget
root = Tk()

root.title("Matt's Image Viewer")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Users/mgermaine93/Desktop/CODE/album-artwork-finder/artwork/",
                                               title="Please select a file", filetypes=(("JPG files", "*.jpg"), ("JPEG files", "*.jpeg"), ("PNG files", "*.png"), ("All files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_button = Button(root, text="Open File", command=open).pack()

root.mainloop()


# e = Entry(root, width=50, bg="green", fg="black")
# e.pack()


# def myClick():
#     myLabel = Label(root, text=f"Hello, {e.get()}")
#     myLabel.pack()


# # # CREATES a label widget within the "root" widget
# # myOtherLabel = Label(root, text="Yo!!!")
# myButton = Button(root, text="Please enter your name:  ", command=myClick)


# # PUTS the label widget on the screen
# # myLabel.pack()
# # myLabel.grid(row=0, column=0)
# # myOtherLabel.grid(row=1, column=1)
# myButton.pack()

# root.mainloop()
