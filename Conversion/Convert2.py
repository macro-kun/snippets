import os
import tkinter as tk
from tkinter import font
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk


WIDTH = 700
HEIGHT = 500

flag = False


def load_image(path):
    global image
    global flag
    global image_label

    if flag:
        image_label.image = None
        image_label.destroy()
        flag = False

    image = Image.open(open(path, "rb"))
    image.thumbnail((500, 400))
    photoImage = ImageTk.PhotoImage(image)
    image_label = tk.Label(labelFrame, image=photoImage)
    image_label.image = photoImage
    image_label.pack()
    flag = True


def drop(event, flag):
    global path
    path = event.data
    load_image(path)


def convert_image():
    try:
        grayed_img = image.convert("L")
    except NameError:
        return
    dir_name = os.path.split(path)
    new_path = dir_name[0] + "/grayed_" + dir_name[1]
    grayed_img.save(new_path)
    load_image(new_path)


root = TkinterDnD.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("グレースケール変換アプリ")

FONT_LABEL = font.Font(family="Noto Sans CJK JP", size=14)

labelFrame = tk.LabelFrame(
    font=FONT_LABEL, width=500, height=400, text="画像をドラッグ&ドロップしてください"
)

labelFrame.drop_target_register(DND_FILES)
labelFrame.dnd_bind("<<Drop>>", lambda event: drop(event, flag))
labelFrame.pack(side=tk.TOP, pady=10)

conv_button = tk.Button(text="変換", font=FONT_LABEL, command=convert_image, width=20)
conv_button.pack(side=tk.BOTTOM, pady=25)


root.mainloop()
