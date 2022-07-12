def ChkCap(Ch):
    if(Ch >= 'A' and Ch <= 'Z' ):
        return True
    else:
        return False    

def main():
    value = input("Enter the chracter : ")[0]
    
    Ret = ChkCap(value)
    if(Ret == True):
        print("Yes ,  it is Capital Alphabet")
    else:
        print("No ,  it is not Capital Alphabet")    

if __name__ == "__main__":
    main()