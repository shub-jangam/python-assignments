def display(no,pattern):
    for i in range(no):
        print(pattern,end = "\t")

def main():
    print("Enter the No ", end = "")
    no = int(input())
    for i in range(1,no+1,1):
            print()
            for j in range(i):
                print("*",end ="")

if __name__ == "__main__":
    main()