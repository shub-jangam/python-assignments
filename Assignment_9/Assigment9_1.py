import threading
import time

def display ():
    for i in range(1,6,1):
        print(i)
t1 = threading.Thread(target= display)
t2 = threading.Thread(target= display)
t3 = threading.Thread(target= display)

t1.start()
time.sleep(1)
t2.start()
time.sleep(1)
t3.start()
time.sleep(1)
