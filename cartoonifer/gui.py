import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import cartoonfier
# making the main windown
top = tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='white')
label = Label(top, background='#CDCDCD', font=('calibri', 20, 'bold'))

# making the cartoonify button in the main window
upload = Button(top, text="Cartoonify an Image", command=cartoonfier.upload(), padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)

# making s save button in the main windown
save1 = Button(top, text="Save cartoon image", command=lambda: cartoonfier.save(ImagePath, ReSized6), padx=30, pady=5)
save1.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
save1.pack(side=TOP, pady=50)

# main function to build the tkinter window
top.mainloop()
