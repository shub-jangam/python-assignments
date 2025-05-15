def getFactor(no):
    result =  list()
    for i in range(1 ,no ,1):
        if no%i ==0:
            result.append(i)
    return result

def main():
    print("Enter No to Check if Its Prime : ")
    no = int(input())
    if no >=1:
        result = getFactor(no)
        if len(result)<2:
            print("Prime Number")
        else:
            print("Not Prime Number")
    else:
        print("Enter No greater then or equal to 1")

if __name__ == "__main__":
    main()