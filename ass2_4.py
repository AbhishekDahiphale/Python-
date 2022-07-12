def AddFactors(No):
    sum = 0
    for i in range(1,int((No/2)+1)):
        if((No%i)==0):
            print(i)
            sum = sum + i
    return sum        


def main():
    value = int(input("Enter the Number"))
    
    Ret = AddFactors(value)
    print("Addition of factors are  : ",Ret)    

if __name__ == "__main__":
    main()