import sys
import os
import time
from DataLogger import createlogFile ,appendMessage



def displayFileWithExtension(DirectoryName , Extesion, logFilename):
    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
        
    print("Absolute path is : "+DirectoryName)

    for foldername, subFoldenames, FilesNames in os.walk(DirectoryName):
        print("folder Name is  " + foldername)
        for fname in FilesNames:
            FileExtention = os.path.splitext(fname)
            if FileExtention[1] == Extesion:
                print("File Name is " + fname)
                appendMessage(logFilename , "File Found with name - " + fname)

def main():
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 3):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory")
            print("Please provide valid absolute path")

        else:
            logFileName = createlogFile("MarvellousLogs",sys.argv[0])
            displayFileWithExtension(sys.argv[1],sys.argv[2] ,logFileName)          

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)

if __name__ == "__main__":
    main()