from StringX import ChkChar

def main():
    String = input("Enter the string : ")
    ch = input("Enter the chracter : ")[0]
    
    Ret = ChkChar(String,ch)
    if(Ret == True):
        print("Character is present in the given string ")
    else:
        print("Character is not present in the given string")    

if __name__ == "__main__":
    main()