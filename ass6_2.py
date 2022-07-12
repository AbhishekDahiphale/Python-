class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Name of Customer : ",self.Name)
        print("Total Amount : ",self.Amount)

    def Deposit(self,Amount):
        self.Amount = self.Amount + Amount

    def Withdraw(self,Amount):
        if(self.Amount < Amount):
            return False
        else:    
            self.Amount = self.Amount - Amount

    def CalculateInterest(self):
        Interest = float((self.Amount * BankAccount.ROI )/100)
        return Interest

def main():
    Name = input("Enter the Name : ")
    Amount = float(input("Enter the Amount : "))

    obj1 = BankAccount(Name,Amount)
    obj1.Display() 
    Deposit = float(input("Enter the Amount to deposit : "))
    obj1.Deposit(Deposit)
    obj1.Display()
    WithDraw = float(input("Enter amount to withdraw : "))
    Ret = obj1.Withdraw(WithDraw)
    if(Ret == False):
        print("Insufficient Amount !!!")
    else:
        obj1.Display()
    Ret = obj1.CalculateInterest()
    print("Interest on availabel amount : ",Ret)

    Name = input("Enter the Name : ")
    Amount = float(input("Enter the Amount : "))

    obj2 = BankAccount(Name,Amount)
    obj2.Display() 
    Deposit = float(input("Enter the Amount to deposit : "))
    obj2.Deposit(Deposit)
    obj2.Display()
    WithDraw = float(input("Enter amount to withdraw : "))
    Ret = obj2.Withdraw(WithDraw)
    if(Ret == False):
        print("Insufficient Amount !!!")
    else:
        obj2.Display()
    Ret = obj2.CalculateInterest()
    print("Interest on availabel amount : ",Ret)            



if __name__ == "__main__":
    main()