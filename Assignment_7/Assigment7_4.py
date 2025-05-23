from functools import reduce

multi_Nos = lambda x,y : x*y

def reduceX(task, data):
    output = 1
    for i in data:
        output = task(output, i)
    return output

def main():

    print("Enter no Item to Add : ")
    no = int(input())
    nolist = list()

    for i in range(no):
        print("Enter No  : ", end = "")
        value = int(input())
        nolist.append(value)

    output = 1

    output = reduceX(multi_Nos,nolist)
    #output = reduce(multi_Nos,nolist)

    print(output)
    

if __name__ == "__main__":
    main()