def ChkNum(no):
    if(no==0):
        return 1
    elif(no > 0):
        return 2
    elif(no < 0):
        return 3
    


def main():
    No = int(input("Entre the Number"))
    Ret = ChkNum(No)
    if(Ret == 2):
        print("Positive Number")
    elif(Ret == 3):
        print("Negative Number")
    elif(Ret == 1):
        print("Zero")

if __name__ == "__main__":
    main()