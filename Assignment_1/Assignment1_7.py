
def ChkNum(no1):
    if ((no1%5) == 0):
        print(True)
    else:
        print(False)


def main():
    print("Enter Number to: " , end="")
    number = int(input())
    ChkNum(number)

if __name__=="__main__":
    main()