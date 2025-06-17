# Write a program that shcedules a function to print "Do coding...!" every 30 minitues.

import schedule
import time

def Do_Coding():
    print(" Do coding Function is running.....")


def main():
    
    schedule.every(30).minutes.do(Do_Coding)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()