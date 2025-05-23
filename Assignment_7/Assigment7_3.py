
chkEven = lambda x : x%2==0

def filtreX(task, data):
    ret = list()
    for i in data:
        if task(i) == True:
            ret.append(i)
    return ret

def main():

    print("Enter no Item to Add : ")
    no = int(input())
    nolist = list()

    for i in range(no):
        print("Enter No  : ", end = "")
        value = int(input())
        nolist.append(value)

    #output = filterX(chkEven,nolist)
    output = list(filter(chkEven,nolist))

    print(output)
    

if __name__ == "__main__":
    main()