import datetime
import hashlib
import time
import schedule
from sys import *
import os

def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()    

def Dublicate_remove(path = argv[1]):
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
                filepath = foldername +"\\"+filen
                unique = hashfile(filepath)
                flag1 = False    
                for key in diction:
                    if diction[key] == unique:
                        file_path = foldername + "\\" + filen
                        os.remove(file_path)
                        flag1 = True

                if flag1 == True:
                    data = str(filen + "\n")
                    fd1 = open(name,'a')
                    fd1.write(data)
                    fd1.close()
                    
                else:
                    diction.update({filen : unique})   
                flag1 = False             
        diction.clear()      

    else:
        print("Invalid Path")

diction = dict()
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
            print("usage : This script is used for the removal of dublicate file")
            exit()

    if (len(argv)==2):
        try:
            #Dir_Dublicate(argv[1])
            schedule.every(1).minute.do(Dublicate_remove)
            while True:
                schedule.run_pending()
                time.sleep(1) 

        except ValueError:
            print("Error : Invalid datatype of input")

        except Exception as e:
            print("Error : ",e)

if __name__ == "__main__":
    main()