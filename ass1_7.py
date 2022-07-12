def Divisible5(no):
    if((no%5)==0):
        return True
    else:
        return False    
    
def main():
    No = int(input("Entre the Number"))
    Ret = Divisible5(No)
    if(Ret == True):
        print("Yes,it is Divisible by 5")
    elif(Ret == False):
        print("No,it is not divisible by 5")

if __name__ == "__main__":
    main()