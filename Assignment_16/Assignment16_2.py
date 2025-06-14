def main():
    print("Enter File name to Display the content's")
    filename =  input()
    with open(filename, 'r') as f1:
        print(f1.read())

if __name__ == "__main__":
    main()