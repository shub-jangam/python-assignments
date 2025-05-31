import threading

def DisplayEven(no):
    for i in range(0, no+1, 1):
        if i%2 ==0:
            print(i)
def DisplayOdd(no):
    for i in range(1,no+1 ,1):
        if i%2 !=0:
            print(i)
def main():
    Even  = threading.Thread(target=DisplayEven, args=(10,))
    Odd   = threading.Thread(target=DisplayOdd, args=(10,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()
