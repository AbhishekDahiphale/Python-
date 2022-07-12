def ChkAlpha(Ch):
    if((Ch >= 'A' and Ch <= 'Z' ) or (Ch >= 'a' and Ch <= 'z')):
        return True
    else:
        return False    

def main():
    value = input("Enter the chracter : ")[0]
    
    Ret = ChkAlpha(value)
    if(Ret == True):
        print("Yes ,  it is Alphabet")
    else:
        print("No ,  it is not Alphabet")    

if __name__ == "__main__":
    main()