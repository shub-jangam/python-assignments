import multiprocessing
import threading
import time

def summ(no):
    sum= 0
    for i in range(no):
        sum =sum +i    
    print(sum)

def main():

    mStartTime = time.time()
    m1 = multiprocessing.Process(target=summ ,args= (100000,))
    m1.start()
    m1.join()
    mEndTime = time.time()
    print("Time Taken to complet multi processing " , mEndTime - mStartTime)

    tStartTime = time.time()
    t1 = threading.Thread(target=summ ,args= (100000,))
    t1.start()
    t1.join()
    tEndTime = time.time()
    print("Time Taken to complet using thread" ,tEndTime - tStartTime)

    StartTime = time.time()
    summ(100000)
    EndTime = time.time()
    print("Time Taken to complet using normal" ,EndTime - StartTime)


if __name__ == "__main__":
    main()