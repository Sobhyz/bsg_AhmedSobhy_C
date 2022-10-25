import threading

def prnta():
    for i in range(100):
        print('a',end='')

def prntb():
    for i in range(100):
        print('b',end='')

t1 = threading.Thread(target=prnta,name='t1')
t2 = threading.Thread(target=prntb,name='t2')

t1.start()
t2.start()
t1.join()
t2.join()