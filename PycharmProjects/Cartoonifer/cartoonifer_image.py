import cv2  # for image processing
import easygui  # to open the filebox
import numpy as np  # to store image
import imageio  # to read image stored at particular path

import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

top = tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='white')
label = Label(top, background='#CDCDCD', font=('calibri', 20, 'bold'))


def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)


def cartoonify(ImagePath):
    # read the image
    img = cv2.imread(ImagePath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(img)

    if img is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()

    resize1 = cv2.resize(img, (960, 540))
    plt.imshow(resize1, cmap='gray')

    # converting an image to grayscale
    gray_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resize2 = cv2.resize(gray_scale_img, (960, 540))
    plt.imshow(resize2, cmap='gray')

    # applying median blur to smoothen an image
    smooth_gray_scale = cv2.medianBlur(gray_scale_img, 5)
    resize3 = cv2.resize(smooth_gray_scale, (960, 540))
    plt.imshow(resize3, cmap='gray')

    # retrieving the edges for cartoon effect using thresholding technique
    getEdge = cv2.adaptiveThreshold(smooth_gray_scale, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)
    resize4 = cv2.resize(getEdge, (960, 540))
    plt.imshow(resize4, cmap='gray')

    # applying bilateral filter to remove noise, keep edge sharp as required
    colorImage = cv2.bilateralFilter(img, 9, 300, 300)
    resize5 = cv2.resize(colorImage, (960, 540))
    plt.imshow(resize5, cmap='gray')

    # masking edged image with our "BEAUTIFY" image
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    resize6 = cv2.resize(cartoonImage, (960, 540))
    plt.imshow(resize6, cmap='gray')

    # Plotting the whole transition
    images = [resize1, resize2, resize3, resize4, resize5, resize6]

    fig, axes = plt.subplots(3, 2, figsize=(8, 8), subplot_kw={'xticks': [], 'yticks': []},
                             gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')

    save1 = Button(top, text="Save cartoon image", command=lambda: save(resize6, ImagePath), padx=30, pady=5)
    save1.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
    save1.pack(side=TOP, pady=50)

    plt.show()


def save(ReSized6, ImagePath):
    # saving an image using imwrite()
    newName = "cartoonified_Image"
    path1 = os.path.dirname(ImagePath)
    extension = os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName + extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))
    I = "Image saved by name " + newName + " at " + path
    tk.messagebox.showinfo(title=None, message=I)


upload = Button(top, text="Cartoonify an Image", command=upload, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)

top.mainloop()
