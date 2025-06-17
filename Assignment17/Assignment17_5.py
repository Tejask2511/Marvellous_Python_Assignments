# Schedule a job that runs every 5 minutes to write the current time to a file Marvellous.txt

import schedule
import time
import datetime
import sys

def Printing_C_time(FileName):
    fobj=open(FileName,'a')
    time=datetime.datetime.now()
    fobj.write(str(time)+"\n")
    fobj.close()


def main():

    FileName=sys.argv[1]
    fobj=open(FileName,'w')
    fobj.close()


    schedule.every(1).minutes.do(Printing_C_time,FileName)
    while True:
        schedule.run_pending()
        time.sleep(1)





if __name__=="__main__":
    main()