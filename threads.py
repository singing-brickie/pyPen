#!/usr/bin/python3

import threading
import time

class myThread(threading.Thread):
    def __init__(self,name,delay):
        threading.Thread.__init__(self)
        self.name=name
        self.delay=delay
    def run(self):
        print(self.name + " is starting")
        count = 0
        while count < 11:
            time.sleep(self.delay)
            print(self.name+" "+str(time.ctime(time.time())))
            count+=1



thread1 = myThread("first",2)
thread2 = myThread("second",1)

thread1.start()
thread2.start()
while(thread2.is_alive()):
    print("are we there yet")
print("waiting on threads 1 and 2")

print("waiting on just 1 thread")
thread1.join()
print("thats them all now")






