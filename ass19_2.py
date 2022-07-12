
def Accept(data,No):
    for i in range(No):
        data.append(int(input())) 

def Display(data):
    for i in range(len(data)):
        print(data[i],end="\t")
    print("")

def Small(data):
    num = data[0]
    for i in range(len(data)):
        if(data[i] < num):
            num = data[i]

    return num                
     

def main():
    value = int(input("How many numbers : "))
     
    data = list()

    Accept(data,value)
    Display(data)

    Ret = Small(data)
    print("Largerst number is : ",Ret)        



if __name__ == "__main__":
    main()