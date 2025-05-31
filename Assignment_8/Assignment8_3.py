import threading

def DisplayEven(inputlist):
    sum = 0
    for i in inputlist:
        if i%2 ==0:
            sum =sum +i
    print("Addition of Even no : ",sum)
def DisplayOdd(inputlist):
    sum = 0
    for i in inputlist:
        if i%2 !=0:
            sum = sum + i 
    print("Additon of ODD no : ", sum)

def main():
    templist = [1,2,3,4,5,6,7,8,9,10]
    Even  = threading.Thread(target=DisplayEven, args=(templist,))
    Odd   = threading.Thread(target=DisplayOdd, args=(templist,))

    Even.start()
    Odd.start()

    # Even.join()
    # Odd.join()

if __name__ == "__main__":
    main()
