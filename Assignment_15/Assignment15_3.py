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
        print("File Already Exist in folder")
    else:
        f = open("ABC.txt" ,mode = 'r')
        data = f.read()
        f.close ()
        
        print("Creating File with "+ filename)
        f2 = open(filename, mode = 'w')
        f2.write(data)
        f2.close()
if __name__ == "__main__":
     main()