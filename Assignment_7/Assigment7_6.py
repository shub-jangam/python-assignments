def ListPrime(no):
    result =  list()
    for i in range(1 ,no ,1):
        if no%i ==0 and i >0 :
            result.append(i)
    if len(result)<2 and (no!= 1 and no!=0):
        return True
    else:
        return False

def filterX (inputlist):
    primenolist = list(filter(ListPrime , inputlist))
    return primenolist

def main():
    print("Enter the Number : ", end = "")
    no = int(input())
    inputlist = list()
    for i in range(no):
        no1 = int(input("Enter Item : "))
        inputlist.append(no1)
    output = filterX(inputlist)
    print(output)
    
if __name__ =="__main__":
    main()