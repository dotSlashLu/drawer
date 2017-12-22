# encoding=utf8
import Tkinter as tk

import conf
import choose


class OperationFrame(tk.Frame):
    def __init__(self, parent, app):
        tk.Frame.__init__(self, parent, bg=conf.BG)
        self.parent = parent
        self.app = app
        self.emp_list = choose.load_list()
        self.choosing = False
        self.bind_all("<space>", self.key)
        self.render()

    def key(self, event):
        if self.choosing == False:
            self.start_choosing()
        else:
            self.stop_choosing()

    def render(self):
        self.pack(fill=tk.X)
        self.result_str = tk.StringVar()
        result_label = tk.Label(self, textvariable=self.result_str,
                                justify=tk.CENTER, width=20)
        result_label.pack(side=tk.LEFT)

        end_btn = tk.Button(self, text=u'结束', width=10,
                            command=self.stop_choosing)
        end_btn.pack(side=tk.RIGHT)

        start_btn = tk.Button(self, text=u'开始', width=10,
                              command=self.start_choosing)
        start_btn.pack(side=tk.RIGHT)


    def choose(self):
        if not self.choosing:
            return
        self.result = choose.get_one(self.emp_list)
        self.result_str.set('%s - %s' % self.result)
        self.app.master.after(conf.CHOOSING_INTERVAL, self.choose)

    def start_choosing(self):
        self.choosing = True
        self.choose()

    def stop_choosing(self):
        if self.choosing == False:
            return
        self.choosing = False
        self.emp_list = self.emp_list - set([self.result])
        self.app.result_frame.add_one(self.result_str.get())

