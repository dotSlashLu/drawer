# encoding=utf8
import Tkinter as tk
import conf

class ResultListFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent, bg=conf.BG)
        self.render()

    def render(self):
        self.pack(fill=tk.BOTH, expand=1)
        scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        listbox = tk.Listbox(self, bg=conf.BG, fg="#ffffff", borderwidth=0,
                             relief=tk.FLAT, highlightthickness=0,
                             yscrollcommand=scrollbar.set)
        self.listbox = listbox
        scrollbar.config(command=self.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.pack(fill=tk.BOTH, expand=1)

    def yview(self, *args):
        apply(self.listbox.yview, args)

    def add_one(self, val):
        self.listbox.insert(0, '%4d. %s' % (self.listbox.size() + 1, val))

