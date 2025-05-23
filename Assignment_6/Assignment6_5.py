def ChkPrime(no):
    ret = "is not Prime No"
    result =  list()
    for i in range(1 ,no ,1):
        if no%i ==0 and i >0 :
            result.append(i)
    if len(result)<2 and (i!= 1 and i!=0):
        ret = "is Prime Number"
    return ret

def main():
    print("Enter the Number : ", end = "")
    no = int(input())
    print(no , ChkPrime(no))

if __name__ =="__main__":
    main()

