# encoding=utf8
import Tkinter as tk
from PIL import Image, ImageTk

import conf


class BannerFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent, bg=conf.BG)
        self.render()

    def render(self):
        self.pack()
        image = Image.open('./assets/banner.gif')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, borderwidth=0)
        label.image = photo
        label.pack(fill=tk.Y)

