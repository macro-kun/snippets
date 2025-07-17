import os
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD


WIDTH = 700
HEIGHT = 500


class ConversionApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        FONT_LABEL = font.Font(family="Noto Sans CJK JP", size=14)

        self.flag = False

        self.title("グレースケール変換アプリ")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.labelFrame = tk.LabelFrame(
            self,
            font=FONT_LABEL,
            width=500,
            height=400,
            text="画像をドラッグ＆ドロップしてください",
        )
        self.labelFrame.drop_target_register(DND_FILES)
        self.labelFrame.dnd_bind("<<Drop>>", self.drop)
        self.labelFrame.pack(side=tk.TOP, pady=10)

        self.conv_button = tk.Button(
            self, text="変換", font=FONT_LABEL, command=self.convert_image, width=20
        )
        self.conv_button.pack(side=tk.BOTTOM, pady=25)

    def clear_image(self):
        self.image_label.image = None
        self.image_label.destroy()

        self.flag = False

    def convert_image(self):
        self.grayed_img = self.image.convert("L")
        dir_name = os.path.split(self.path)
        new_path = dir_name[0] + "/grayed_" + dir_name[1]
        self.grayed_img.save(new_path)
        self.load_image(new_path)

    def drop(self, event):
        self.path = event.data
        self.load_image(self.path)

    def load_image(self, file_path):

        if self.flag:
            self.clear_image()

        self.image = Image.open(open(file_path, "rb"))
        self.image.thumbnail((500, 400))
        self.photoImage = ImageTk.PhotoImage(self.image)

        self.image_label = tk.Label(self.labelFrame, image=self.photoImage)
        self.image_label.image = self.photoImage
        self.image_label.pack()

        self.flag = True


if __name__ == "__main__":
    app = ConversionApp()
    app.mainloop()
