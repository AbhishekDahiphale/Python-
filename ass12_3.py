from datetime import *
import time
from unicodedata import name
import schedule
import psutil
import os
from sys import *

def create_log(dir,listprocess):
    file_name = "Marvellous%s.log"%time.time()
    Complete_Name = os.path.join(dir,file_name)
    fd = open(Complete_Name,"w")
    des = "-"*80
    fd.write(des+"\n")
    fd.write(str("Process time : %s"%time.ctime))
    fd.write(des+"\n")
    for elem in listprocess:
        fd.write(str(elem)+"\n")
    fd.close    


def Process_Monitor_log(dir=argv[1]):
    listprocess = list()
    
    if not os.path.exists(dir):
        os.mkdir(dir)
    else:
        pass    

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['memory'] = proc.memory_info().vms / (1024*1024)
            listprocess.append(pinfo)
        except Exception:
            pass    
    
    create_log(dir,listprocess)   


def main():
    print("---- Abhishek Dahiphale-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (len(argv)==2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("usage : ApplicationName Directory_name")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : This Script is used to create log file of process information which are running")
            exit()

    if (len(argv)==2):
        try:
            #Process_Monitor_log()
            schedule.every(1).minute.do(Process_Monitor_log)
            while True:
                schedule.run_pending()
                time.sleep(1)
        except ValueError:
            print("Value Error")

        except Exception as e: 
            print("Error : ",e)
if __name__ == "__main__":
    main()               