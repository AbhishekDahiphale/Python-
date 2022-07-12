def CountDigit(value):
    icnt=0
    while(value!=0):
        idigit = int(value%10)
        value = int(value/10)
        icnt = icnt+1
    return icnt    




def main():
    value = int(input("Enter the Number"))
    Ret = CountDigit(value)
    print("Digit Count is : ",Ret)    

if __name__ == "__main__":
    main()
    