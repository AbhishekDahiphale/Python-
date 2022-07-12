
from sys import *
import hashlib

def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while(len(buf)>0):
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()    

def ChkContent(File1,File2):
    f1 = hashfile(File1)
    f2 = hashfile(File2)

    if f1 == f2:
        return True 
    else:
        return False    


def main():
    print("Automation script Name : ",argv[0])


    if len(argv) > 3 or len(argv)< 2 : 
        print("Invalid number of arguments ")
        print("use -h flag for help ")
        print("use -u flag for usage ")

    if(len(argv)==2):
        if argv[1] == "-u" or argv[1] == "-U":
            print("Usage : Check both file contents same or not ")
            exit()

        elif argv[1] == "-h" or argv[1] == "-H":
            print("Help : Name_of_Script First_Argument Second_Argument")
            print("First_Argument : File_Name")
            print("Second_Argument : File_Name")
            exit()

        else:
            print("There is no such flag ")
            exit()    

    if len(argv) == 3:
        File1 = argv[1]
        File2 = argv[2]

        Ret = ChkContent(File1,File2)

        if(Ret == True):
            print("content is same in the file")
        else:
            print("Content is not same")    



if __name__ == "__main__":
    main()