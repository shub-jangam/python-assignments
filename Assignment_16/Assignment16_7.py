def main():
    filename =  "marks.txt"
    with open(filename, 'r') as f1:
        for line in f1:
            templist = line.split(",")
            if int(templist[1]) > 75:
                print("name : " + templist[0])

if __name__ == "__main__":
    main()