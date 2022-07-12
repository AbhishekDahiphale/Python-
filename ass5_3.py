
class Arithimatic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

    def Addition(self):
        return int(self.value1 + self.value2)

    def Subtraction(self):
        return int(self.value1 - self.value2)

    def Multiplication(self):
        return int(self.value1 * self.value2)

    def Division(self):
        if(self.value2 == 0):
            return -1

        return float(self.value1/self.value2)                        

def main():
    No1 = int(input("Eneter the first Number : "))
    No2 = int(input("Enter the second Number : "))

    obj1 = Arithimatic()
    obj1.Accept(No1,No2)
    
    Ret = obj1.Addition()
    print("Addition is : ",Ret)
    
    Ret = obj1.Subtraction()
    print("Subtraction is : ",Ret)

    Ret = obj1.Multiplication()
    print("Multiplication is : ",Ret)

    Ret = obj1.Division()
    print("Division is : ",Ret)

    No1 = float(input("Eneter the first Number : "))
    No2 = float(input("Enter the second Number : "))

    obj2 = Arithimatic()
    obj2.Accept(No1,No2)
    
    Ret = obj2.Addition()
    print("Addition is : ",Ret)
    
    Ret = obj2.Subtraction()
    print("Subtraction is : ",Ret)

    Ret = obj2.Multiplication()
    print("Multiplication is : ",Ret)

    Ret = obj2.Division()
    print("Division is : ",Ret)

    
if __name__ == "__main__":
    main()