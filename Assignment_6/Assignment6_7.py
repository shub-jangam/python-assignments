    
def main():
    inputvalues = list()

    for i in range(5):
        print("Enter a Number : ", end = "")
        no1 =  int(input())  
        inputvalues.append(no1)

    output = 0

    for i in inputvalues:
        if i> output:
            output = i
    print(output)

if __name__ =="__main__":
    main()