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

    if(len(sys.argv) == 1):
        if((sys.argv[0] == "--h") or (sys.argv[0] == "--H")):
            print("This application is gives active process running on system ")

        elif((sys.argv[0] == "--u") or (sys.argv[0] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py")
        else:
            logFileName = createlogFile(sys.argv[0],sys.argv[0], ".txt", "")
            processList= ProcessDisplay()
            if len(processList)>0:
                for value in processList:
                        info = f"Process Name {value['name']} PID number is {str(value['pid'])}, and username is{value['username']}"
                        appendMessage(logFileName,info) 
            else: 
                appendMessage(logFileName,"No Active process found")       

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