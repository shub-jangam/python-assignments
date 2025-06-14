import schedule
import datetime
import time

def CheckEmail():
    print("Checking Email!!")

def main():
    schedule.every(10).seconds.do(CheckEmail)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
