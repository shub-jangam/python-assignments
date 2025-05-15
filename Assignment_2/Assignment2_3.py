def factorial(no):
    result = 1
    for i in range(no,0,-1):
        result = result * i
    return result


def main():
    print("Enter Number : ", end = "")
    no1 = int(input())
    output= factorial(no1)
    print("factorial " ,output)

if __name__=="__main__":
    main()
