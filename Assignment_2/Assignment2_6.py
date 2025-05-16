def display(no,pattern):
    for i in range(no):
        print(pattern,end = "\t")

def main():
    print("Enter the No ", end = "")
    no = int(input())
    for i in range(no,0,-1):
        display(i,"*")
        print()

if __name__ == "__main__":
    main()