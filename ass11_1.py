import datetime
import hashlib
import time
import schedule
from sys import *
import os

def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    print(afile)
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()    

def Checksum(path = argv[1]):
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
                print("File name is : ",filen)
                filepath = foldername +"\\"+filen
                unique = hashfile(filepath)
                print("Checksum of "+filen+" file : ",unique)
                print(' ')

    else:
        print("Invalid Path")

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
            print("usage : This Script is used to display checksum of all file which are present in the given directory")
            exit()

    if (len(argv)==2):
        try:
            Checksum()
            """"schedule.every(1).minute.do(Checksum)
            while True:
                schedule.run_pending()
                time.sleep(1)""" 

        except ValueError:
            print("Error : Invalid datatype of input")

        except Exception as e:
            print("Error : ",e)

if __name__ == "__main__":
    main()