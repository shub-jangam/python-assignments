import schedule
import datetime
import time

def fun_min():
    print("currentTime")
    print(datetime.datetime.now())
    data = datetime.datetime.now()
    
    with open("demo.txt",'a') as f1:
        f1.write("currentTime : " +str(data)+ "\n")
        f1.close()

def main():
    schedule.every(1).minute.do(fun_min)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
