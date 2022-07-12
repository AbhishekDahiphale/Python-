import datetime
import shutil
import time
import schedule
from sys import *
import os
i=0


def Copy_dir(path=argv[1] ,dir=argv[2]):
    print("Current time is : ",datetime.datetime.now())
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    global i
    dir = dir + "_" + str(i)
    i=i+1
    os.mkdir(dir)
    exists = os.path.isdir(path)
    
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)

            for filen in filname:
                source = path +"\\" +filen
                dest = dir +"\\"+filen
                shutil.copy(source,dest)
                print("Copied.....")
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
            print("usage : ApplicationName AbsolutePath_of_Directory Directory_Name ")
            print("AbsolutePath_of_Directory : Exsiting Directory Name")
            print("Directory_Name : Create for new Directory")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : This Script is used to Copy all files from all directory and paste to the other Directory")
            exit()

    if (len(argv)==3):
        try:
            #Copy_dir(argv[1],argv[2])
            schedule.every(1).minute.do(Copy_dir)
            while True:
                schedule.run_pending()
                time.sleep(1) 

        except ValueError:
            print("Error : Invalid datatype of input")

        except Exception as e:
            print("Error : ",e)

if __name__ == "__main__":
    main()
