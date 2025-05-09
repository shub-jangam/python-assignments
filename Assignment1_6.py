
def ChkNum(no1):
    if no1>0:
        print("Positive Number")
    elif no1 < 0 :
        print("Negative Number")
    else:
        print("zero Number")

def main():
    print("Enter Number to: " , end="")
    number = int(input())
    ChkNum(number)

if __name__=="__main__":
    main()