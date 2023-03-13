from classifier import Classifier
import sys
import os
import tkinter as tk
import PIL
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from fastai.vision.core import PILImage
from tkinter import messagebox

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Yummy Classifier")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=350, height=200)
    canvas.grid(columnspan=3, rowspan=5)

    # logo
    logo = Image.open('logo.jpg')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=1, row=0)

    # info
    instructions = tk.Label(root, text="Select a jpg/png file to check if it looks yummy or not")
    instructions.grid(columnspan=3, column=0, row=1)

    # button logic
    def open_file():
        browse_text.set("loading...")
        file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Images", ".jpg .png")])
        browse_text.set("Try again")
        img = PILImage.create(file)

        classifier = Classifier()
        #yummy, probability = classifier.isYummyFromPath(imagePath)
        yummy, probability = classifier.isYummy(img)

        if yummy:
            messagebox.showinfo("Results", "LOOKS GREAT!!\nProbability it's yummy: %.5f \nIt would fit right in https://reddit.com/r/foodporn" % probability)
        else:
            messagebox.showinfo("Results", "DISGUSTING!!\nProbability it's yummy: %.5f \nTake that away to https://reddit.com/r/shittyfoodporn" % probability)

    # button
    m = tk.StringVar()
    browse_text = tk.StringVar()
    browse_button = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font="Raleway",
                                bg="#20bebe", fg="white", height=1, width=20)
    browse_text.set("Choose file")
    browse_button.grid(column=1, row=2)

    canvas = tk.Canvas(root, width=350, height=10)
    canvas.grid(columnspan=3)

    root.mainloop()