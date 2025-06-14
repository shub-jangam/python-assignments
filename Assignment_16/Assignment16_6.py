def main():
    sourceFile = "C:\\gitRepo\\python-assignments\\Assignment_15\\demo.txt"
    destinationFile = "dest.txt"

    with open(sourceFile , 'r') as sourceFile , open(destinationFile  ,'w') as destinationFile:
        destinationFile.write(sourceFile.read())

if __name__ == "__main__":
    main()