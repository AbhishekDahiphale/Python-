
class Numbers:
    def __init__(self,Value):
        self.Value = Value

    def ChkPrime(self):
        flag = True
        for i in range(2,int(self.Value/2)):
            if(self.Value%i == 0):
                flag = False
                break
        return flag

    def ChkPerfect(self):
        sum = 0
        for i in range(1,int(self.Value/2)+1):
            if(self.Value%i == 0):
                sum = sum + i

        if(sum == self.Value):
            return True
        else:
            return False

    def SumFactors(self):    
        sum = 0
        for i in range(1,int(self.Value/2)+1):
            if(self.Value%i == 0):
                sum = sum + i

        return sum

    def Factors(self):
        data = list()
        for i in range(1,int(self.Value/2)+1):
            if(self.Value%i == 0): 
                data.append(i)

        return data
                    

def main():
    value = int(input("Enter the number : "))

    obj1 = Numbers(value)
    Ret = obj1.ChkPrime()
    if(Ret == True):
        print("Number is prime")
    else:
        print("Number is not Prime")

    Ret = obj1.ChkPerfect()
    if(Ret == True):
        print("Number is Perfect")
    else:
        print("Number is not Perfect")

    Ret = obj1.SumFactors()
    print("Sum of all factors : ",Ret)

    Ret = obj1.Factors()
    print("Factors of Number : ",Ret)   

    value = int(input("Enter the number : "))

    obj2 = Numbers(value)
    Ret = obj2.ChkPrime()
    if(Ret == True):
        print("Number is prime")
    else:
        print("Number is not Prime")

    Ret = obj2.ChkPerfect()
    if(Ret == True):
        print("Number is Perfect")
    else:
        print("Number is not Perfect")

    Ret = obj2.SumFactors()
    print("Sum of all factors : ",Ret)

    Ret = obj2.Factors()
    print("Factors of Number : ",Ret)       




if __name__ == "__main__":
    main()