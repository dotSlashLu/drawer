#!python
# encoding=utf8
import sys
import time
import random
import threading
import Tkinter as tk
import traceback
from PIL import Image, ImageTk

from choose import ChoosingThread


__author__ = 'zhangqiang'

WINDOW_TITLE = '祝君好运，今晚吃鸡'
BG = '#114A3D'


class Application():
    def __init__(self, master):
        self.master = master
        master.geometry('{}x{}'.format(460, 350))
        master.protocol("WM_DELETE_WINDOW", self.on_app_close)
        master.configure(background=BG)
        try:
            self.render()
            
        except Exception as e:
            traceback.print_exc()
            print e

    def render(self):
        self.banner_frame = BannerFrame(self.master)
        self.operation_frame = OperationFrame(self.master)

    def on_app_close(self):
        print('on close called')
        self.operation_frame.on_app_close()
        self.master.destroy()
        sys.stdout.flush()
        sys.exit()


class BannerFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent, bg=BG)
        self.render()

    def render(self):
        self.pack()
        image = Image.open('./assets/banner.gif')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, borderwidth=0)
        label.image = photo
        label.pack(fill=tk.Y)


class OperationFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent, bg=BG)
        self.choosing_t = None
        self.init_evs()
        self.render()

    def init_evs(self):
        self.events = {
            'choosing': threading.Event(),
            'destroy_choosing': threading.Event()
        }

    def render(self):
        self.pack()
        start_btn = tk.Button(self, text=u'开始', width=10,
                              command=self.start_choosing)
        start_btn.pack(side=tk.LEFT)

        end_btn = tk.Button(self, text=u'结束', width=10,
                            command=self.stop_choosing)
        end_btn.pack(side=tk.LEFT)

        self.result = tk.StringVar()
        result_label = tk.Label(self, textvariable=self.result,
                                justify=tk.CENTER, width=20)
        result_label.pack(side=tk.LEFT)

    def start_choosing(self):
        if not self.choosing_t:
            self.choosing_t = ChoosingThread(result=self.result,
                                             ev=self.events)
            self.choosing_t.deamon = True
            self.choosing_t.start()

        self.events['choosing'].set()

    def stop_choosing(self):
        self.events['choosing'].clear()

    def on_app_close(self):
        self.events['choosing'].set()
        self.events['destroy_choosing'].set()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.title(WINDOW_TITLE)
    root.iconbitmap('./assets/favicon.ico')
    root.mainloop()
