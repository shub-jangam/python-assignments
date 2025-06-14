def CheckFileExist(filename):
    try:
        with open(filename, "r") as f:
            return True
    except FileNotFoundError:
        return False

def main():
    print("Enter the File name  ")
    filename  = input()
    exist = CheckFileExist(filename)
    if exist ==True:
        print("File Exist in Folder !!")
    else:
        print("File not found in Folder")

if __name__ == "__main__":
    main()