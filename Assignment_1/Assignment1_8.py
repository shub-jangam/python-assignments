
def displayMsg(no1 , mesaage ="*"):
    for i in range(no1):
        print(mesaage ,end = "\t")


def main():
    print("Enter Number: " , end="")
    number = int(input())
    displayMsg(number)

if __name__=="__main__":
    main()