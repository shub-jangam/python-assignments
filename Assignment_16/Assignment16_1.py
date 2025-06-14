def main():
    print("Enter the File Name : ")
    filename = input()

    with open(filename , 'a') as f1:
        for i in range(5):
            name  = input("Enter Student name : ")
            f1.write(name + "\n")
        f1.close()
if __name__ == "__main__":
    main()
