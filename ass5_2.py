
class Cicle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self,Radius):
        self.Radius = Radius

    def CalculateArea(self):
        self.Area = float(Cicle.PI *(self.Radius * self.Radius))

    def CalculateCirumference(self):
        self.Circumference = float(2 * (Cicle.PI * self.Radius))

    def Display(self):
        print("Radius of Cicle : ",self.Radius)
        print("Area of Circle : ",self.Area)
        print("Circumference of Cicle : ",self.Circumference)    

def main():
    value = float(input("Enter the Radius : "))

    obj1 = Cicle()
    obj1.Accept(value)
    obj1.CalculateArea()
    obj1.CalculateCirumference()
    obj1.Display()

    value = float(input("Enter the Radius : "))

    obj2 = Cicle()
    obj2.Accept(value)
    obj2.CalculateArea()
    obj2.CalculateCirumference()
    obj2.Display()



if __name__ == "__main__":
    main()