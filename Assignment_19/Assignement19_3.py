import sys
import os
import time
from DataLogger import createlogFile ,appendMessage
import shutil



def DirectoryCopyExt(DirectoryName, newDirectoryName, logFilename):
    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)
        newDirectoryName = os.path.abspath(newDirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    # create Directroy 
    os.makedirs(newDirectoryName, exist_ok=True)

    print("Absolute path is : "+DirectoryName)

    for foldername, subFoldenames, FilesNames in os.walk(DirectoryName):
        for fname in FilesNames:
            sourcePath = os.path.join(DirectoryName , fname)
            distPath = os.path.join(newDirectoryName, fname)
            with open(sourcePath, 'rb') as sourcefile:
                with open(distPath, 'wb') as destinationfile:
                    destinationfile.write(sourcefile.read())
                    appendMessage(logFilename ,f"File copied successfully from {DirectoryName} to {newDirectoryName} file name {fname}" )

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
            DirectoryCopyExt(sys.argv[1],sys.argv[2] ,logFileName)          

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