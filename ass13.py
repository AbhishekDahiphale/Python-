from sys import *
import schedule
from ass13_Module import *          


def main():
    print("---------Abhishek Dahiphale-------")
    print("Name of the Script : ",argv[0])

    if len(argv)!=4:
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

    if len(argv) == 4:
        try:
            #DublicateFileRemoval()
            Minute = int(argv[2])
            schedule.every(Minute).minutes.do(DublicateFileRemoval)
            while True:
                schedule.run_pending()
                time.sleep(1)
        except ValueError as v:
            print("Value : ",v)
        except Exception as e:
            print("Exception  : ",e)

if __name__ == "__main__":
    main()
