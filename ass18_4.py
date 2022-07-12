def Accept(data,No):
    for i in range(No):
        data.append(int(input())) 

def Display(data):
    for i in range(len(data)):
        print(data[i],end="\t")
    print("")    
     

def main():
    value = int(input("How many numbers : "))
     
    data = list()

    Accept(data,value)
    Display(data)

    No1 = int(input("Enter the first Number : "))
    No2 = int(input("Enter the second Number : "))

    Ret = list(filter(lambda no : (No1 < no < No2),data))
    if(len(Ret) == 0):
        print("Numbers are not present !!")
    else:
        print("Numbers present at given range : ",Ret)        



if __name__ == "__main__":
    main()