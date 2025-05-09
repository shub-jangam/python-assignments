
def ChkNum(no1):
    if no1%2==0:
        print("Even Number")
    else:
        print("odd Number")

def main():
    print("Enter Number to: " , end="")
    number = int(input())
    ChkNum(number)

if __name__=="__main__":
    main()