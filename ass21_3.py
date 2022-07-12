def Display(ch):
    temp = ord(ch)
    if('A' <= ch <= 'Z' ):
        for i in range(temp,ord('Z')+1):
            print(ch,end='\t')
            ch = chr(ord(ch)+1)
    elif('a' <= ch <= 'z' ):
        for i in range(temp,ord('a')-1,-1):
            print(ch,end='\t') 
            ch = chr(ord(ch)-1)      
    print("")         

def main():
    value = input("Enter the chracter : ")[0]

    Display(value)


if __name__ == "__main__":
    main()