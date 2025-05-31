import functools
customfilter =  lambda x : x>=70 and x<=90
custommap = lambda x : x+10
customReduce = lambda x,y : x*y

def main():
    templist = [4,34,36,76,68,24,89,23,86,90,45,70]

    flist= list(filter(customfilter,templist))
    print("List after filter",flist)
    mlist= list(map(custommap,flist))
    print("List after map",mlist)
    reduce = functools.reduce(customReduce,mlist)
    print("Output",reduce)


if __name__ == "__main__":
    main()    