from multiprocessing import Process
import time
import os


def build():
    while True:
        d = time.localtime()
        if (d.tm_hour == 4 and d.tm_min == 40):
            pass
        if request == Ture:
            pass
        
if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=build)
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'
