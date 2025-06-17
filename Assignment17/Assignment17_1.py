# Write a python scripts that prints " jay Ganesh.." every 2 seconds.use the schedule.every(2).do(..)function

import schedule
import time

def printfunc():
    print("Jay Ganesh....")


def main():
    
    schedule.every(2).seconds.do(printfunc)
    while True:
        schedule.run_pending()
        time.sleep(1)
    


if __name__=="__main__":
    main()