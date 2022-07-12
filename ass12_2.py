import time
from unicodedata import name
import schedule
import psutil
import os
from sys import *

def DisplaySpecificProcess(Process_Name=argv[1]):
    listprocess = list()
    Process_Name = str(Process_Name + '.exe')
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            if Process_Name == pinfo['name']:    
                listprocess.append(pinfo)
                break
        except Exception:
            pass    
    
    for elem in listprocess:
            print(elem)

def main():
    print("---- Abhishek Dahiphale-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (len(argv)==2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("usage : ApplicationName Process_Name")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : This Script is used to display the specific process information which are running")
            exit()

    if (len(argv)==2):
        try:
            #DisplaySpecificProcess()
            schedule.every(1).minute.do(DisplaySpecificProcess)
            while True:
                schedule.run_pending()
                time.sleep(1)
        except Exception as e: 
            print("Error : ",e)
if __name__ == "__main__":
    main()               