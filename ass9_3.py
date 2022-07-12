from ast import arg
import os
from sys import *

def create(name):
    if os.path.exists(name):
        return False
    else:
        fd = open(name,"x")
        return fd

def copy(source,dest):
    fd1 = open(source,"r")
    fd2 = open(dest,"w")

    data = fd1.read()
    fd2.write(data)


def main():
    var = argv[1]

    if len(argv) == 2:
        if var == "-h" or var == "-H":
            print("Help : File_Name Existing_File_Name")
            exit

        elif var == "-u" or var == "-U":
            print("usage : copy data from one file to another file")
            exit()
        
        else:
            print("There is no such flag")


    else:
        print("Invalid number of arguments")
        exit()


    dest = input("Enter the name to create the file : ")

    fd = open(dest,"x")
    if fd == False:
        print("File is already exist")
        exit()

    source = argv[1]

    copy(source,dest)

    fd = open(dest,"r")
    data = fd.read()
    print("Copied data : ",data)



if __name__ == "__main__":
    main()