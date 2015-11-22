import threading
import datetime
class mythread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID=counter
        self.name=name
        self.counter=counter

    def run(self):
        print "Starting " + self.name
        print_date(self.name, self.counter)
        print "Exiting " + self.name

def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print "%s[%d]: %s" % ( threadName, counter, datefields[0] )

t1=mythread("thread1",1)
t2=mythread("thread2", 2)

t1.start()
t2.start()

t1.join()
t2.join()

print "hello world"

