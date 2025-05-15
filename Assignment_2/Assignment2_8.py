def display(no):
    for i in range(no):
        print(i+1,end = "\t")
        


def main():
    print("Enter the No ", end = "")
    no = int(input())
    for i in range(1 , no+1 ,1):
        display(i)
        print()

if __name__ == "__main__":
    main()