def Chksmall(Ch):
    if(Ch >= 'a' and Ch <= 'z' ):
        return True
    else:
        return False    

def main():
    value = input("Enter the chracter : ")[0]
    
    Ret = Chksmall(value)
    if(Ret == True):
        print("Yes ,  it is Small Alphabet")
    else:
        print("No ,  it is not Small Alphabet")    

if __name__ == "__main__":
    main()