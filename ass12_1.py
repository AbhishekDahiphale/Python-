import time
import schedule
import psutil
import os
from sys import *

def ProcessDisplay():
    listprocess = list()

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])

            listprocess.append(pinfo)
        except Exception:
            pass    

    return listprocess

def main():
    print("---- Abhishek Dahiphale-----")

    print("Application name : " +argv[0])

    if (len(argv) != 1):
        print("Error : Invalid number of arguments")
        exit()
    
    if (len(argv)==2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("usage : ApplicationName")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : This Script is used to display the all process information which are running")
            exit()

    if (len(argv)==1):
        
        listProcess = ProcessDisplay()

        for elem in listProcess:
            print(elem)

        

if __name__ == "__main__":
    main()               