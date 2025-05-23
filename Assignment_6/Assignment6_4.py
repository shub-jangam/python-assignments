
def main():
    print("Enter the Number : ", end = "")
    no = int(input())
    output = 1

    for i in range(no,0,-1):
        output = output * i
    print( output)

if __name__ =="__main__":
    main()

