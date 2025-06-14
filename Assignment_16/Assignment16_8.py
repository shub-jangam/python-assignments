def main():
    filename =  "abc.txt"
    newdata = []
    with open(filename, 'r') as f1:
        lines = f1.readlines()
        for line in lines:
            if line.strip() != '':
                newdata.append(line)
    print(newdata)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(newdata)
        

if __name__ == "__main__":
    main()