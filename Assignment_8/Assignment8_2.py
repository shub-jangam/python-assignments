import threading

def DisplayEven(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0: 
            if i % 2 == 0:
                sum =sum + i 
    print("Addition of Even no : ",sum)

def DisplayOdd(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0: 
            if i % 2 != 0:
                sum =sum + i 
    print("Addition of Even no", sum)



def main():
    Even  = threading.Thread(target=DisplayEven, args=(20,))
    Odd   = threading.Thread(target=DisplayOdd, args=(20,))

    Even.start()
    Odd.start()

if __name__ == "__main__":
    main()
