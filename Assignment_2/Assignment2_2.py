def display(no1,pattern):
    for i in range(no1):
        print(pattern,end = "\t")
        


def main():
    print("Enter the No ",end = "")
    no1 = int(input())
    for i in range(no1):
        display(no1,"*")
        print()

if __name__ == "__main__":
    main()