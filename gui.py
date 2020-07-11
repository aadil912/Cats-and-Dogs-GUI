from tkinter import filedialog
from tkinter import *

#load the trained model to classify sign
# MODEL_NAME = cats_dogs.h5
win = Tk()
win.geometry('1024x768')
win.title("Detect Cats and Dogs")

label = Label(win, text='Covid-19 Detection', font=("Arial", 35))
label.grid(row=0, column=0)

button = Button(win, text='Upload your Image', padx=30, pady=8)
button.grid(row=1, column=0)
win.mainloop()



