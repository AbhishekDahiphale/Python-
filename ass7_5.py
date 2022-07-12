def Factorail(No):
    if(No!=1):
        No = No * Factorail(No-1)
    return No    


     

def main():
    value = int(input("Enter the Number : "))
    Ret = Factorail(value)
    print("Factoraila are : ",Ret)

if __name__ == "__main__":
    main()