# Schedule a task that displays current date and time every minute using the datetime module.
import time
import schedule
import datetime

def CurrentDateTime():
    time=datetime.datetime.now()
    print(time)


def main():
    schedule.every(1).minutes.do(CurrentDateTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

    
    

if __name__=="__main__":
    main()


