class Demo:
    Value = 10

    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2

    def fun(self):
        print("Inside instance method fun")
        print("Value of No1 : ",self.No1)
        print("Value of No2 : ",self.No2)

    def Gun(self):
        print("Inside instance method gun")
        print("Value of No1 : ",self.No1)
        print("Value of No2 : ",self.No2)        



def main():
    value1 = int(input("Eneter the first number : "))
    value2 = int(input("Eneter the second number : "))

    obj1= Demo(value1,value2)
    obj1.fun()
    obj1.Gun()

    value1 = int(input("Eneter the first number : "))
    value2 = int(input("Eneter the second number : "))

    obj2 = Demo(value1,value2)
    obj2.fun()
    obj2.Gun()


if __name__ == "__main__":
    main()