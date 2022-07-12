from socket import timeout
from sys import argv
import webbrowser
from  urllib.request import urlopen
import re

def is_connected():
    try:
        urlopen("https://www.google.co.in/",timeout=1)
        return True
    except Exception as e:
        print("Exception : ",e)
        return False  

def Find(string):
    url = re.findall ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)         
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            url = Find(line)
            print(url)
            for str in url:
                webbrowser.open(str,new=2)

def main():
    print("---Abhishke Dahiphale-----")
    print("Script Name : ",argv[0])

    if len(argv)!=2:
        print("Error : Invalid Number of arguments")
        exit()

    if argv[1] == "-h" or argv[1] == "-H":
        print("This Script is used to open url which are written in one file")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage : Application_Name Name_Of_the_file")
        exit()

    if len(argv)==2:
        try:
            connected = is_connected()

            if connected:
                WebLauncher(argv[1])
            else:
                print("Unable To Connect The Internet....")
        except ValueError as e:
            print("Error  : ",e)
        except Exception as e:
            print("Error  : ",e)    

if __name__ == "__main__":
    main()