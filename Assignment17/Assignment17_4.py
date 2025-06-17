# Create a task that run once every day At 9:00 Am and print "Namaskar...."

import schedule
import time

def Greet():
    print(" Namaskar....")

def main():
    schedule.every().day.at("09:00").do(Greet)
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__=="__main__":
    main()