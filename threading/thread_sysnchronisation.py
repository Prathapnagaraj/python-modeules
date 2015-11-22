__author__ = 'pbillava'

import threading

class Mythread(threading.Thread):
    def __init__(self, name, value, pattern):
        threading.Thread.__init__(self)
        self.name=name
        self.value=value
        self.pattern=pattern*value

    def run(self):
        lock.acquire()
        print self.pattern
        print "this thread name %s value %s \n"%(self.name, self.value)
        print self.pattern
        print "this thread name %s value %s \n"%(self.name, self.value)
        print self.pattern
        print "this thread name %s value %s \n"%(self.name, self.value)
        print self.pattern
        print "this thread name %s value %s \n"%(self.name, self.value)
        print self.pattern
        print "this thread name %s value %s \n"%(self.name, self.value)
        print self.pattern
        print "this thread name %s value %s \n"%(self.name, self.value)
        lock.release()

t1=Mythread("thread1",10,"*")
t2=Mythread("thread2",20,"#")
t3=Mythread("thread3",30,"$")

lock=threading.Lock()
thread_pool=[]
for t in [t1,t2,t3]:
    thread_pool.append(t)
    t.start()

for t in thread_pool:
    t.join()

print "hello world"



