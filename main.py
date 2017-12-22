#!python
# encoding=utf8
import sys
import time
import traceback
import Tkinter as tk

import conf
from ui.frame_banner import BannerFrame
from ui.frame_operation import OperationFrame
from ui.frame_result import ResultListFrame


__author__ = 'zhangqiang'


class Application():
    def __init__(self, master):
        self.master = master
        master.geometry('{}x{}'.format(*conf.WINDOW_SIZE))
        master.protocol("WM_DELETE_WINDOW", self.on_app_close)
        master.configure(background=conf.BG)
        try:
            self.render()

        except Exception as e:
            traceback.print_exc()
            print e

    def render(self):
        self.banner_frame = BannerFrame(self.master)
        self.operation_frame = OperationFrame(self.master, self)
        self.result_frame = ResultListFrame(self.master)

    def on_app_close(self):
        print('on close called')
        self.master.destroy()
        sys.stdout.flush()
        sys.exit()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.title(conf.WINDOW_TITLE)
    root.iconbitmap(conf.WINDOW_ICON)
    root.mainloop()
