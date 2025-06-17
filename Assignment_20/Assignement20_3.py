import sys
import os
import time
from DataLogger import createlogFile ,appendMessage
import hashlib



def calculate_checksum(path):
    fobj = open (path, 'rb')
    hobj = hashlib.md5()
    buffer = fobj.read(100)

    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(100)

    fobj.close()
    return hobj.hexdigest()

def DirectoryDublicateRemoval(DirectoryName,logFilename):
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

    chckSumlist = []

    for foldername, subFoldenames, FilesNames in os.walk(DirectoryName):
        for fname in FilesNames:
            sourcePath = os.path.join(DirectoryName , fname)
            ret = calculate_checksum(sourcePath)
            if ret in chckSumlist:
                os.remove(sourcePath)
                appendMessage(logFilename , f"{fname} is deleted from {DirectoryName}" )
            else:
                chckSumlist.append(ret)
def main():
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory")
            print("Please provide valid absolute path")

        else:
            logFileName = createlogFile(sys.argv[0],sys.argv[0])
            DirectoryDublicateRemoval(sys.argv[1],logFileName)          

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