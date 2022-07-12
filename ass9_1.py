
import os

def search(name):
    if os.path.exists(name):
        return True
    else:
        return False       
    
def main():
    name = input("enter the file name to search : ")

    ret = search(name)
    if ret == True:
        print("File is exist in the current directory")
    else:
        print("file was not found in the current directory")    

if __name__ == "__main__":
    main()