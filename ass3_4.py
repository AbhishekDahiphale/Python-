def Frequency(data,No):
    cnt = 0

    for i in range(len(data)):
        if(No == data[i]):
            cnt = cnt + 1

    return cnt        

def Display(data):

    for i in range(len(data)):
        print(data[i],end="  ")

    print()    


def Accept(data,size):

    for i in range(size):
        data.append(int(input()))


def main():
    size = int(input("Number of elements : "))

    data = []
     
    Accept(data,size)

    print("Elements are : ")
    Display(data)

    value = int(input("Enter the number to count frequency : "))  

    iRet = Frequency(data,value)
    print("Frequency of '",value,"' in the list are : ",iRet)


if __name__ == "__main__":
    main()