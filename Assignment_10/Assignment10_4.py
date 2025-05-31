import functools
customfilter =  lambda x : x%2==0
custommap = lambda x : x**2
customReduce = lambda x,y : x+y


def main():
    templist = [] #[4,34,36,76,68,24,89,23,86,90,45,70]
    try :
        print("Enter Size of List : ")
        num = int(input())
        for i in range(num):
            print("Enter the no : ")
            no = int(input())
            templist.append(no)
        flist= list(filter(customfilter,templist))
        print("List after filter",flist)
        mlist= list(map(custommap,flist))
        print("List after map",mlist)
        reduce = functools.reduce(customReduce,mlist)
        print("Output",reduce)
    except Exception as eobj:
        print("Error Ocurred While accepting input !!", eobj)

if __name__ == "__main__":
    main()

