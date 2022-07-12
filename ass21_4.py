def ChkSymbol(ch):
    ch = ord(ch)
    if(ch >= 21 and ch <= 47):
        return True
    else:
        return False     

def main():
    value = input("Enter the chracter : ")[0]

    Ret = ChkSymbol(value)
    if(Ret == True):
        print("It is a Symbol")
    else:
        print("It is not Symbol")    


if __name__ == "__main__":
    main()