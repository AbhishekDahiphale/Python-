
def Accept(data,No):
    for i in range(No):
        data.append(int(input())) 

def Display(data):
    for i in range(len(data)):
        print(data[i],end="\t")
    print("")

def Diff(data):
    large = data[0]
    small = data[0]
    for i in range(len(data)):
        if(data[i] < small):
            small = data[i]
        elif(data[i] > large):
            large = data[i]

    return (large-small)                
     

def main():
    value = int(input("How many numbers : "))
     
    data = list()

    Accept(data,value)
    Display(data)

    Ret = Diff(data)
    print("Difference between large and small number : ",Ret)        



if __name__ == "__main__":
    main()