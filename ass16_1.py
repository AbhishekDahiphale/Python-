def Accept(data,No):
    for i in range(No):
        data.append(int(input())) 

def Display(data):
    for i in range(len(data)):
        print(data[i],end="\t")
    print("")    

def Diff(data):
    even = 0
    odd = 0
    for i in range(len(data)):
        if(data[i]%2 == 0):
            even = even + data[i]
        else:
            odd = odd + data[i]

    return (even - odd)            



def main():
    value = int(input("How many numbers : "))

    data = list()

    Accept(data,value)
    Display(data)

    Ret = Diff(data)
    print("Differnce between summation of odd and even elements : ",Ret)



if __name__ == "__main__":
    main()