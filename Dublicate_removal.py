import time
from sys import *
import hashlib
import os

def Write_log(List):
    dirName = "Marvellous"
    if not os.path.isdir(dirName):
        os.mkdir(dirName)
    else:
        pass

    Log_file = "%s.log"%time.time() 
    Logfile_path = os.path.join(dirName,Log_file)
    design = "*"*80
    start_data = "Scrpt information : %s"%time.ctime()
    fd = open(Logfile_path,'a')
    fd.write(design+"\n")
    fd.write("\n"+start_data+"\n\n")
    fd.write(design+"\n\n")
    for file in List:
        print()
        data = file + "\n"
        fd.write(data)
    fd.close()
    #Mail_Sender(Log_file,argv[3])

def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DublicateFileRemoval(dir=argv[1]):
    diction = dict()
    removal_list = list()
    if not os.path.isabs(dir):
        dir = os.path.abspath(dir)

    exists = os.path.isdir(dir)
    if exists:
        for foldername,subfolder,filename in os.walk (dir):
            for filen in filename:
                Mk_path = os.path.join(foldername,filen)
                unique = hashfile(Mk_path)
                flag = False
                for key in diction:
                    if diction[key] == unique:
                        removal_list.append(filen)          
                        flag = True
                        os.remove(Mk_path)
                if flag == False:
                    diction.update({filen : unique})
        Write_log(removal_list)  
    else:
        print("Invalide Path")              
                  

def main():
    print("---------Abhishek Dahiphale-------")
    print("Name of the Script : ",argv[0])

    if len(argv)!=2:
        print("Invalid Number of command line arguments")
        print("For The help use -h ")
        print("For the usgae of script use -u")

    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage : This script is used to Remove the dublicate file and create the log file which store inforamtion of remove file and send that file through mail")

    if argv[1] == "-h" or argv[1] == "-H":
        print("Arguments Sequence should be -> : Application_name Directory_Name Minutes Mail")
        print("Directory : Pass the directory Exsiting path")
        print("Minutes : Time to run script after given minutes")
        print("Main : Mail which have to send to given mail(Receiver mail)")

    if len(argv) == 2:
        try:
            DublicateFileRemoval()
            """ Minute = int(argv[2])
            schedule.every(Minute).minutes.do(DublicateFileRemoval)
            while True:
                schedule.run_pending()
                sleep(1)"""
        except ValueError as v:
            print("Value : ",v)
        except Exception as e:
            print("Exception  : ",e)




if __name__ == "__main__":
    main()