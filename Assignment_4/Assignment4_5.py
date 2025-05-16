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
    z = [2,70,11,10,17,103,31,77] 
    print(z)
    flist= list(filter(ListPrime,z))
    print("List after filter",flist)
    mlist= list(map(custommap,flist))
    print("List after map",mlist)
    reduce = functools.reduce(customReduce,mlist)
    print("output",reduce)

if __name__ == "__main__":
    main()