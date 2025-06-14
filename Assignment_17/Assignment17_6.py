import schedule
import datetime
import time
def lunch():
    print(" Lunch Time!!")
def up():
    print("Wrap up work !!")

def main():
    schedule.every().day.at("16:21").do(lunch)
    schedule.every().day.at("16:23").do(up)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
