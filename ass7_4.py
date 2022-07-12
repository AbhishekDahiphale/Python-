def SumDigitR(No,sum=0):
    if(No!=0):
        Digit = int(No%10)
        No = int(No /10)
        sum = sum + Digit + SumDigitR (No,sum)
    return sum
        
     

def main():
    value = int(input("Enter the digit : "))
    Ret = SumDigitR(value)
    print("Sum of Digit are : ",Ret)

if __name__ == "__main__":
    main()