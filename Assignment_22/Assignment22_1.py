import sys
import os
import time
from DataLogger import createlogFile ,appendMessage
import emailUtil
import hashlib
import schedule
import re


def validEmailID(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def calculate_checksum(path):
    fobj = open (path, 'rb')
    hobj = hashlib.md5()
    buffer = fobj.read(1024)

    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()

def DirectoryDublicateRemoval(DirectoryName,scriptName,recipentEmail):

    logFileName = createlogFile(FileName=scriptName ,ScriptName = scriptName, ext =".txt",FolderName="Mavellous")

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
    dublicate_file_count = 0
    total_file_count = 0

    for foldername, subFoldenames, FilesNames in os.walk(DirectoryName):
        for fname in FilesNames:
            sourcePath = os.path.join(DirectoryName ,foldername, fname)
            total_file_count = total_file_count+1
            ret = calculate_checksum(sourcePath)
            if ret in chckSumlist:
                dublicate_file_count = dublicate_file_count + 1 
                os.remove(sourcePath)
                appendMessage(logFileName, f"{fname} is deleted from {sourcePath}" )
            else:
                chckSumlist.append(ret)
    if dublicate_file_count ==0:
        appendMessage(logFileName, "No doublicate file found !!" )
    
    message = f"Total Number of file Scan is {total_file_count} and dublicate file found are {dublicate_file_count}"
    
    try:
        emailUtil.sendEmail(subject="LogFile", attachment_file_path= logFileName, receiver_email=recipentEmail, emailBody=message)
    except Exception as e:
        print(f'Failed to send email: {e}')

def main():
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 4):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory scheduleTimeInMin Email ID" )
            print("Please provide valid absolute path")

        else:
            schedule.every(int(sys.argv[2])).minutes.do(DirectoryDublicateRemoval ,sys.argv[1],sys.argv[0],sys.argv[3])
            while True:
                schedule.run_pending()
                time.sleep(1)
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