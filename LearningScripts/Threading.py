#!/usr/bin/env python3
# coding:utf8

""" 
https://pybay.com/site_media/slides/raymond2017-keynote/threading.html#david-baron-at-mozillas-san-francisco-office 
"""


import threading
import queue

###########################################################################################

enable_threading = False
counter = 0

counter_queue = queue.Queue()


def counter_manager():
    'I have EXCLUSIVE rights to update the counter variable'
    global counter

    while True:
        increment = counter_queue.get()
        counter += increment
        print_queue.put(['The count is %d' % counter, '---------------'])
        counter_queue.task_done()


t = threading.Thread(target=counter_manager)
t.daemon = enable_threading
t.start()
del t

###########################################################################################

print_queue = queue.Queue()


def print_manager():
    'I have EXCLUSIVE rights to call the "print" keyword'

    while True:
        job = print_queue.get()
        for line in job:
            print(line)
        print_queue.task_done()


t = threading.Thread(target=print_manager)
t.daemon = enable_threading
t.start()
del t

###########################################################################################


def worker():
    'My job is to increment the counter and print the current count'
    counter_queue.put(1)


print_queue.put(['Starting up'])
worker_threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    worker_threads.append(t)
    t.start()
for t in worker_threads:
    t.join()

counter_queue.join()
print_queue.put(['Finishing up'])
print_queue.join()
