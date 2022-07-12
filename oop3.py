class Assignment3:
    def __init__(self,size):
        self.data = list()
        self.size = size

    def Accept(self):
        for i in range(self.size):
            self.data.append(int(input()))

    def Display(self):        
        print("Elemets are :")  
        for i in range(self.size):
            print(self.data[i],end="\t")

        print("")

    def Addition(self):
        add = 0
        for i in range(self.size):
            add = add + self.data[i]

        return add 

    def Maximum(self):
        max = self.data[0]
        for i in range(1,self.size):
            if(max < self.data[i]):
                max = self.data[i]

        return max

    def Minimum(self):
        min = self.data[0]
        for i in range(1,self.size):
            if(min > self.data[i]):
                min = self.data[i]

        return min 

    def Frquency(self,No):
        icnt = 0
        for i in range(self.size):
            if(No == self.data[i]):
                icnt = icnt + 1

        return icnt

    @staticmethod
    def ChkPrime(Value):
        flag = True
        for i in range(2,int(Value/2)+1):
            if(Value%i == 0):
                flag = False
                break
        return flag

    def SumPrime(self):
        sum = 0
        for i in range(self.size):
            if(Assignment3.ChkPrime(self.data[i])!=False):
                sum = sum + self.data[i]

        return sum 


def main():
    size = int(input("Enter the size : "))

    obj = Assignment3(size)
    obj.Accept()
    obj.Display()
    
    Ret = obj.Addition()
    print("Addition of all number are : ",Ret)

    Ret = obj.Maximum()
    print("Largest Number is : ",Ret)

    Ret = obj.Minimum()
    print("Smlalest Number is : ",Ret)

    No = int(input("Eneter the number to know frequency : "))
    Ret = obj.Frquency(No)
    print("Frquency of given number is : ",Ret)

    Ret = obj.SumPrime()
    print("Additio of all prime numbers : ",Ret)


if __name__ == "__main__":
    main()