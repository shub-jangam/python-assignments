def main():
    filename =  "abc.txt"
    with open(filename, 'r') as f1:
        for line in f1:
            templist = line.split(" ")
            if len(templist) > 5:
                print(line)

if __name__ == "__main__":
    main()