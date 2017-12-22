# encoding=utf8
import time
import random
import threading


__author__ = 'zhangqiang'

INTERVAL = 0.05


class ChoosingThread(threading.Thread):
    def __init__(self, result, ev):
        threading.Thread.__init__(self)
        self.result = result
        self.ev = ev
        self.load_list()

    def load_list(self):
        with open('./assets/employee_list.txt', 'r') as f:
            content = f.read()
            self.employee_list = [r.split() for r in content.split('\n') if r]
            # print self.employee_list

    def get_one(self):
        return random.choice(self.employee_list)

    def run(self):
        while True:
            if self.ev['destroy_choosing'].is_set():
                return
            self.ev['choosing'].wait()
            time.sleep(INTERVAL)
            uid, name = self.get_one()
            self.result.set('%s - %s' % (uid, name))
