from ast import arg
import datetime
import time
import schedule
from sys import *
import os

def Greater_size(path = argv[1]):
    start = time.time()
    fd = open(name,'a')
    fd.write(str(datetime.datetime.now())+'\n')
    fd.close()
    
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
                size = os.path.getsize(foldername+"\\"+filen)    
                if size > 1000000:
                    data = str(filen) +"\n"
                    fd1 = open(name,'a')
                    fd1.write(data)
                    fd1.close()            

    else:
        print("Invalid Path")
    fd2 = open(name,'a')
    fd2.write("Run Timing for Script : "+str(time.time()-start)+"\n")
    fd2.close()

name = "log.txt"
file = open(name,'x')

def main():
    print("---- Abhishek Dahiphale-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (len(argv)==2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("usage : ApplicationName AbsolutePath_of_Directory")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : This script is used for the Display Highest size file name")
            exit()

    if (len(argv)==2):
        try:
            #Greater_size(argv[1])
            schedule.every(1).minute.do(Greater_size)
            while True:
                schedule.run_pending()
                time.sleep(1) 

        except ValueError:
            print("Error : Invalid datatype of input")

        except Exception as e:
            print("Error : ",e)

if __name__ == "__main__":
    main()