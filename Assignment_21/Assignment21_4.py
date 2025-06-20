import sys
from DataLogger import createlogFile ,appendMessage
import psutil
import smtplib
from email.message import EmailMessage
import os
import re



def validEmailID(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
    
def sendEmail(subject, receiver_email ,attachment_file_path ,sender_email = "abc@example.com"):
    
    try:
        email_password = os.environ['email_password']
        print(email_password)
    except KeyError:
        print("environment variable not found.")

    msg = EmailMessage()
    msg.set_content("Please find the logfile in the attchment.")
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with open(attachment_file_path, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='text', subtype='plain', filename=file_name)


    try:
        with smtplib.SMTP(smtp_server="smtp.gmail.com", smtp_port=587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, email_password)
            smtp.send_message(msg)
            print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

def GetProcessInfo():
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

    if(len(sys.argv) == 3):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to Send the ProcessLog to Email")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  FolderName  Email ID")
            print("Please provide valid FolderName  and Email ID")
        else:
            receiver_email = sys.argv[2]
            if validEmailID(receiver_email):
                logFileName = createlogFile(sys.argv[0],sys.argv[0],FolderName=sys.argv[1])
                processList = GetProcessInfo()
                if len(processList)>0:
                    for value in processList:
                            info = f"Process Name {value['name']} PID number is {str(value['pid'])}, and username is{value['username']}"
                            appendMessage(logFileName,info) 
                else: 
                    appendMessage(logFileName,"No Active process found for")
                sendEmail(receiver_email=receiver_email,attachment_file_path=logFileName,subject=f"LogFile :Active Process")
            else:
                print("Invalid email id provied")

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