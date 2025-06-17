# Write a script that shcedule multiples task: 
# one to print " lunch time!" at 1PM,and another to print "Wrap pn work" at 6 PM .

import schedule
import time

def LuchTime():
    print(" luch Time ")


def WrapWork():
    print(" Wrap Work ")


def main():

    schedule.every().day.at("01:00").do(LuchTime)

    schedule.every().day.at("06:00").do(WrapWork)
    while True:
        schedule.run_pending()
        time.sleep(1)




if __name__=="__main__":
    main()