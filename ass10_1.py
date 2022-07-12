import datetime
import time
import schedule
from sys import *
import os

def DirectoryWatcher(path = argv[1],ext = argv[2]):
    print("Current time is : ",datetime.datetime.now())
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)

            for filen in filname:
                split = os.path.splitext(filen)
                if split[1] == ext:
                    print("File inside "+foldername+"is : "+filen)
                    print(' ')

    else:
        print("Invalid Path")

def main():
    print("---- Abhishek Dahiphale-----")

    print("Application name : " +argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (len(argv)==2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("usage : ApplicationName AbsolutePath_of_Directory Extension")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : This Script is used to traverse specific directory")
            exit()

    if (len(argv)==3):
        try:
            schedule.every(1).minute.do(DirectoryWatcher)
            while True:
                schedule.run_pending()
                time.sleep(1) 

        except ValueError:
            print("Error : Invalid datatype of input")

        except Exception:
            print("Error : Invalid input")

if __name__ == "__main__":
    main()
