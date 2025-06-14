import schedule
import datetime
import time
logfile = "log.txt"

def backupFile():
    print("file back up done !!")
    with open(logfile, 'a') as log:
        log.write("CurrentTime : "+str(datetime.datetime.now())+ " - LogMessage" +"\n")

def main():
    schedule.every(1).hour.do(backupFile)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
