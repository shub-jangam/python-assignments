import time

Border = "-"*54
timestamp = time.ctime()

def createlogFile(FileName, ScriptName,ext ="log"):
    
    filename = FileName.replace(".py","Logs_")
    filename = filename+"%s" %(timestamp)
    filename = filename+ext
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    fobj = open(filename,"w")

    
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Scripts\n")
    fobj.write("This is a "+ ScriptName+" Script\n")

    # fobj.write(Border+"\n")
    # fobj.write("This is is created at \n"+timestamp+"\n")
    # fobj.write(Border+"\n")
    return filename

def appendMessage(logFile , message):
    with open(logFile ,"a") as log_File:
        log_File.write(Border+"\n")
        log_File.write("This is is created at \t "+timestamp+"\t" + message + "\n")
        log_File.write(Border+"\n")



