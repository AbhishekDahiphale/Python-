import datetime
import time
import schedule
from sys import *
import os

def Change_Ext(path=argv[1] ,ext1=argv[2],ext2=argv[3]):
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
                dir=path + "\\" + filen
                if split[1] == ext1:
                    os.rename(dir,split[0]+ext2)
                    print("Done!!!")
    else:
        print("Invalid Path")

def main():
    print("---- Abhishek Dahiphale-----")

    print("Application name : " +argv[0])

    if (len(argv) != 4):
        print("Error : Invalid number of arguments")
        exit()
    
    if (len(argv)==2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("usage : ApplicationName AbsolutePath_of_Directory Extension1 Extension2")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : This Script is used to change the extension of directory")
            exit()

    if (len(argv)==4):
        try:
            #Change_Ext(argv[1],argv[2],argv[3])
            schedule.every(1).minute.do(Change_Ext)
            while True:
                schedule.run_pending()
                time.sleep(1) 

        except ValueError:
            print("Error : Invalid datatype of input")

        except Exception as e:
            print("Error : ",e)

if __name__ == "__main__":
    main()
