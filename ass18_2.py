def Accept(data,No):
    for i in range(No):
        data.append(int(input())) 

def Display(data):
    for i in range(len(data)):
        print(data[i],end="\t")
    print("")    

def FirstOcc(data,No):
    flag = -1
    for i in range(len(data)):
        if(data[i] == No):
            flag = i+1
            break      
    return flag      

def main():
    value = int(input("How many numbers : "))
     
    data = list()

    Accept(data,value)
    Display(data)

    No = int(input("Enter the number to search : "))
    Ret = FirstOcc(data,No)
    if(Ret == -1):
        print("Number is not present")
    else:
        print("Number is present first at ",Ret," index")    



if __name__ == "__main__":
    main()