# write a script that simulates checking for email updates every 10 seconds.
# (use print statement like checking mail.."insted of real email logic  )

import time 
import schedule

def CheckEmail():
    print(" CHeking mail....")


def main():

    schedule.every(10).seconds.do(CheckEmail)
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__=="__main__":
    main()
