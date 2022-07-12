def AddDigit(value):
    sum=0
    while(value!=0):
        digit = int(value%10)
        sum = sum + digit
        value = int(value/10)
        
    return sum    

def main():
    value = int(input("Enter the Number"))
    Ret = AddDigit(value)
    print("Addition of Digit is : ",Ret)    

if __name__ == "__main__":
    main()
    