import schedule
import datetime
import time
def fun():
    print("Do Coding!!")

def main():
    schedule.every(30).minute.do(fun)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
