import os 

def CheckFileExist(filename):
    if os.path.exists(filename):
            return True
    return False

def main():

    print("Enter the filename")
    file1 = input()
    print("Enter the filename")
    file2 = input()

    f1_exist = CheckFileExist(file1)
    f2_exist = CheckFileExist(file2)

    if f1_exist ==True and f2_exist == True:
        print("File Exist in folder")
        with open(file1 , mode = 'r') as f1 , open (file2 , mode= 'r') as f2:  
            if (print(f1.read() == f2.read())):
                 print("Sucessful")
            else:
                 print("failed")
    else:
         print("file didnt exist !!")
if __name__ == "__main__":
     main()