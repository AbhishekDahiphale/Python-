from Arithimatic import *

def main():
    value1 = float(input("Enter the first value"))
    value2 = float(input("Enter the second value"))

    Ret = Add(value1,value2)
    print("Addition is : ",Ret)

    Ret = sub(value1,value2)
    print("Subtraction is : ",Ret)

    Ret = Mult(value1,value2)
    print("Multiplication is : ",Ret) 

    Ret = Div(value1,value2)
    print("Division is : ",Ret)
    


if __name__ == "__main__":
    main()