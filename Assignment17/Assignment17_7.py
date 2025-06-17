# Schedule a function that performs file backup every hour and writes a log entry into backup_log.txt

import time
import schedule
import datetime


def backup():
    t=datetime.datetime.now()
    print("taking file backup")
    logfile=open("backup_log.txt",'a')
    content=str(t)
    logfile.write("Backup taken:\n")
    logfile.write(content)
    logfile.close()



def main():
    logfile = open("backup_log.txt",'w')
    logfile.write("this files contains log of file backup")
    logfile.close()

    schedule.every(1).hour.do(backup)
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__=="__main__":
    main()
