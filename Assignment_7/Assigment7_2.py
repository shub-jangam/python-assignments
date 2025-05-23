task = lambda x : x**2

def mapX(task, data):
    ret = list()
    for i in data:
        ret.append(task(i))
    return ret

def main():

    print("Enter no Item to Add : ")
    no = int(input())
    nolist = list()

    for i in range(no):
        print("Enter No  : ", end = "")
        value = int(input())
        nolist.append(value)

    #output = mapX(task,nolist)
    output = list(map(task,nolist))

    print(output)
    

if __name__ == "__main__":
    main()