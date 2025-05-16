import functools
customfilter =  lambda x : x%2==0
custommap = lambda x : x**2
customReduce = lambda x,y : x+y

def main():
    templist = [5,2,3,4,3,4,1,2,8,10]

    flist= list(filter(customfilter,templist))
    print("List after Filter",flist)
    mlist= list(map(custommap,flist))
    print("List after map",mlist)
    reduce = functools.reduce(customReduce,mlist)
    print("Output",reduce)


if __name__ == "__main__":
    main()