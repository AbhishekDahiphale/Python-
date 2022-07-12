def ChkPrime(No):
    flag = True
    for i in range(2,int((No/2)+1)):
        if(No%i==0):
            flag=False

    return flag

def main():
    value = int(input("Enter the Number"))
    
    Ret = ChkPrime(value)

    if(Ret == True):
        print("Number is prime")
    else:
        print("Number is not prime")        

if __name__ == "__main__":
    main()