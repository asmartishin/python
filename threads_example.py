#!/usr/bin/env python


import Queue
import threading
import time

exit_flag = 0

class MyThread(threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q

    def run(self):
        print('Starting ' + self.name)
        process_data(self.name, self.q)
        print('Exiting' + self.name)


def process_data(thread_name, q):
    while not exit_flag:
        queue_lock.acquire()
        if not work_queue.empty():
            data = q.get()
            queue_lock.release()
            print('%s processing %s' % (thread_name, data))
        else:
            queue_lock.release()
        time.sleep(1)

thread_list = ["Thread-1", "Thread-2", "Thread-3"]
name_list = ["One", "Two", "Three", "Four", "Five"]

queue_lock = threading.Lock()
work_queue = Queue.Queue(10)
threads = []
thread_id = 1

for t_name in thread_list:
    thread = MyThread(thread_id, t_name, work_queue)
    thread.start()
    threads.append(thread)
    thread_id += 1

queue_lock.acquire()
for word in name_list:
    work_queue.put(word)
queue_lock.release()

while not work_queue.empty():
    pass

exit_flag = 1

for t in threads:
    t.join()

print('Exit main thread')

# threading
# import thread
# import time
# def print_time(thread_name, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print '%s: %s' % (thread_name, time.ctime(time.time()))
#
# try:
#     thread.start_new_thread(print_time, ('Thread-1', 2, ))
#     thread.start_new_thread(print_time, ('Thread-2', 4, ))
# except:
#     print 'Unable to start thread'
#
# while 1:
#     pass

# synchronize threads
# import time
# import threading
# exit_flag = 0
#
#
# class MyThread(threading.Thread):
#     def __init__(self, thread_id, name, counter):
#         threading.Thread.__init__(self)
#         self.thread_id = thread_id
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print('Starting ' + self.name)
#         thread_lock.acquire()
#         print_time(self.name, self.counter, 3)
#         thread_lock.release()
#
#
# def print_time(thread_name, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print("%s: %s" % (thread_name, time.ctime(time.time())))
#         counter -= 1
#
# thread_lock = threading.Lock()
# threads = []
#
# thread1 = MyThread(1, 'Thread-1', 1)
# thread2 = MyThread(2, 'Thread-2', 2)
#
# thread1.start()
# thread2.start()
#
# threads.append(thread1)
# threads.append(thread2)
#
# for t in threads:
#     t.join()
# print('Exiting main thread')




