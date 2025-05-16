from MarvellousNum import ChkPrime
from Assignment3_1 import listadd


def ListPrime(templist):
    primeNOList = list()
    for i in templist:
        listofelem = ChkPrime(i)
        if len(listofelem)<2 and (i!= 1 and i!=0):
            primeNOList.append(i)
    return primeNOList

        
def main():
    print("Input :  Number of Element ")
    no =  int(input())
    templist = list()
    
    for i in range(no):
        print("Input Element : ")
        userInput = int(input())
        templist.append(userInput)
    
    # Check if Number is prime and 
    primeNOList = ListPrime(templist)
    print(primeNOList)
    output = listadd(primeNOList)
    print("Addition of prime Numbers : ", output)

if __name__ == "__main__":
    main()