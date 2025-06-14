import os 

def CheckFileExist(filename):
    if os.path.exists(filename):
            return True
    return False

def main():
    count = 0
    print("Enter the filename with Extention ")
    filename  = input()
    print("Enter the String")
    data = input()
    exist = CheckFileExist(filename)
    if exist ==True:
        print("File found !!")
        f2 = open(filename, mode = 'r')
        filedata = f2.read()
        f2.close()
        tempData = filedata.split()
        print(tempData)
        for i in tempData:
            if data == i:
                 count = count + 1         
    else:
        print("file not found !!")
    print(count)
    
if __name__ == "__main__":
     main()