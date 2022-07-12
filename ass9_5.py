import os
from sys import *

def FreqCount(File,word):
    fd = open(File,"r")
    cnt = 0

    for i in fd:
        words = i.split(" ")

        for j in words:
            if word == j:
                cnt = cnt + 1

    return cnt                  
    


def main():
    print("Automation script Name : ",argv[0])


    if len(argv) > 3 or len(argv)< 2 : 
        print("Invalid number of arguments ")
        print("use -h flag for help ")
        print("use -u flag for usage ")

    if(len(argv)==2):
        if argv[1] == "-u" or argv[1] == "-U":
            print("Usage : Frequency of word in the file ")
            exit()

        elif argv[1] == "-h" or argv[1] == "-H":
            print("Help : Name_of_Script First_Argument Second_Argument")
            print("First_Argument : File_Name")
            print("Second_Argument : word")
            exit()

        else:
            print("There is no such flag ")
            exit()    


    if len(argv) == 3:
        File = argv[1]
        word = argv[2]
        if os.path.exists(File):
            Ret = FreqCount(File,word)
            print("Frequency of given word is : ",Ret)
            
        else:
            print("There is no such file ")
            
            
            


if __name__ == "__main__":
    main()    