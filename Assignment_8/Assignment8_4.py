import threading

def getNumOfSmalllet(data):
    print("Small Tread ID : " , threading.get_ident())
    sum = 0 
    for i in data:
        smalllet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        if i in smalllet:
            sum = sum+1
    print("Small let No : " , sum)

def getNumOfCapitallet(data):
    sum = 0 
    print("Cpital Thread ID :", threading.get_ident())
    for i in data:
        capitallet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        if i in capitallet:
            sum = sum+1
    print("Captial let No : " , sum)

def getNumOfDigit(data):
    sum = 0 
    print("Digit Thread ID : ", threading.get_ident())
    for i in data:
        smalllet = ['1','2','3','4','5','6','7','8','9','0']
        if i in smalllet:
            sum = sum+1
    print("Digit let No : " , sum)
def main():
    data = "Shubham2024"
    
    small  = threading.Thread(target=getNumOfSmalllet, args=(data,))
    capital   = threading.Thread(target=getNumOfCapitallet, args=(data,))
    digit   = threading.Thread(target=getNumOfDigit, args=(data,))

    small.start()
    capital.start()
    digit.start()

    # small.join()
    # capital.join()
    # digit.join()

if __name__ == "__main__":
    main()
