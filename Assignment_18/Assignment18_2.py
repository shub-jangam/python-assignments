import os 

def CheckFileExist(filename):
    if os.path.exists(filename):
            return True
    return False

def main():
    print("Enter the filename with Extention ")
    filename  = input()
    exist = CheckFileExist(filename)
    if exist ==True:
        print("File Exist in Folder !!")
        f = open(filename ,mode = 'r', encoding= 'utf-8')
        print(f.read())
        f.close
    else:
        print("File not found in Folder")

if __name__ == "__main__":
    main()