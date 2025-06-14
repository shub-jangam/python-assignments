import schedule
import datetime
import time
def fun():
    print("Namaskar !!")

def main():
    schedule.every().day.at("09:00").do(fun)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
