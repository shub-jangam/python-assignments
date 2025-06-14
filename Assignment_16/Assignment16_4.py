def main():
    #print("Enter the File Name : ")
    filename = "numbers.txt"

    with open(filename , 'a') as f1:
        for i in range(10):
            name  = input("Enter Number : ")
            f1.write(name + "\n")
        f1.close()
if __name__ == "__main__":
    main()
