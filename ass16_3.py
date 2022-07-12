def Accept(data,No):
    for i in range(No):
        data.append(int(input())) 

def Display(data):
    for i in range(len(data)):
        print(data[i],end="\t")
    print("")    

def EvenDiv5(no):
    if(no%2 == 0 and no%5 == 0):
        return True

def main():
    value = int(input("How many numbers : "))

    data = list()

    Accept(data,value)
    Display(data)

    Ret = list(filter(EvenDiv5,data))
    print("elements Which are even and divisible by 5 : ",Ret)



if __name__ == "__main__":
    main()