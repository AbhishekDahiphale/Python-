def ChkDigit(Ch):
    if(ord(Ch) >= 48 and ord(Ch) <= 57 ):
        return True
    else:
        return False    

def main():
    value = input("Enter the chracter : ")[0]
    
    Ret = ChkDigit(value)
    if(Ret == True):
        print("Yes ,  it is Digit")
    else:
        print("No ,  it is not Digit")    

if __name__ == "__main__":
    main()