import datetime
import shutil
import time
import schedule
from sys import *
import os

i=0

def Copy_Specific_dir(path=argv[1] ,dir = argv[2],ext = argv[3]):
    print("Current time is : ",datetime.datetime.now())
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    global i 
    dir = argv[2]+"_"+str(i)
    i=i+1
    os.mkdir(dir)
    exists = os.path.isdir(path)
    
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)

            for filen in filname:
                split = os.path.splitext(filen)
                if split[1] == ext:
                    source = path +"\\" +filen
                    dest = dir +"\\"+filen
                    shutil.copy(source,dest)
                    print("Copied.....")
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
            print("Help : Application_Name AbsolutePath_of_Director Name_To_Create _Directory Specific_Extension")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : copy specific type of file into another directory")
            exit()

    if (len(argv)==4):
        try:
            #Copy_Specific_dir(argv[1],argv[2],argv[3])
            schedule.every(1).minute.do(Copy_Specific_dir)
            while True:
                schedule.run_pending()
                time.sleep(1) 

        except ValueError:
            print("Error : Invalid datatype of input")

        except Exception as e:
            print("Error : ",e)

if __name__ == "__main__":
    main()
