import functools

def ListPrime(no):
    result =  list()
    for i in range(1 ,no ,1):
        if no%i ==0 and i >0 :
            result.append(i)
    if len(result)<2 and (no!= 1 and no!=0):
        return True
    else:
        return False
custommap = lambda x: x*2
customReduce = lambda x,y: x if x>y else y

def main():
    templist = [] #[4,34,36,76,68,24,89,23,86,90,45,70]
    try :
        print("Enter Size of List : ")
        num = int(input())
        for i in range(num):
            print("Enter the no : ")
            no = int(input())
            templist.append(no)
        flist= list(filter(ListPrime,templist))
        print("List after filter",flist)
        mlist= list(map(custommap,flist))
        print("List after map",mlist)
        reduce = functools.reduce(customReduce,mlist)
        print("Output",reduce)
    except Exception as eobj:
        print("Error Ocurred While accepting input !!", eobj)

if __name__ == "__main__":
    main()

