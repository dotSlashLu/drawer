# encoding=utf8
import sys
import time
import random
import hashlib
import threading


__author__ = 'zhangqiang'

INTERVAL = 0.05


def load_list():
    with open('./assets/employee_list.txt', 'r') as f:
        content = f.read()
        h = hashlib.sha256()
        h.update(content)
        print 'employee list file hash: %s' % h.hexdigest()
        sys.stdout.flush()
        # use set so that each tuple has exactly one chance
        employee_list = set([tuple(r.split()) for r in
                            content.split('\n') if r])
        return employee_list

def get_one(employee_list):
    res = random.choice(list(employee_list))
    return res

