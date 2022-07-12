from sys import *
import subprocess


def ProcessLauncher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            subprocess.run(line)    


def main():
    print("---Abhishke Dahiphale-----")
    print("Script Name : ",argv[0])

    if len(argv)!=2:
        print("Error : Invalid Number of arguments")
        exit()

    if argv[1] == "-h" or argv[1] == "-H":
        print("This Script is used to open process")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage : Application_Name Name_Of_the_file_which_Contains_path_of_application")
        exit()

    if len(argv)==2:
        try:
            ProcessLauncher(argv[1])
            #subprocess.run(argv[1])
        except ValueError as e:
            print("Error  : ",e)
        except Exception as e:
            print("Error  : ",e) 

if __name__ == "__main__":
    main()