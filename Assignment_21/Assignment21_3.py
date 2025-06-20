import sys
from DataLogger import createlogFile ,appendMessage
import psutil

def ProcessDisplay():
    Border = "*"*25
    print(Border)
    print("Information of currently running processess : ")
    print(Border)

    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(info)
        except Exception:
            print("Exception occured")
    return listprocess

def main():
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to GetProcessInfoByName")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  FolderName")
            print("Please provide valid FolderName")
        else:
            logFileName = createlogFile(sys.argv[0],sys.argv[0],".txt",FolderName=sys.argv[1])
            processName = sys.argv[1].lower() + ".exe"
            processList = ProcessDisplay(processName)
            if len(processList)>0:
                for value in processList:
                        info = f"Process Name {value['name']} PID number is {str(value['pid'])}, and username is{value['username']}"
                        appendMessage(logFileName,info) 
            else: 
                appendMessage(logFileName,"No Active process foound for "+ processName)       
    else:
        print("Invalid number of comand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)

if __name__ == "__main__":
    main()