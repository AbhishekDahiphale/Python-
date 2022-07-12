def Minimum(data):
    Min = data[0]

    for i in range(1,len(data)):
        if(Min > data[i]):
            Min = data[i]  

    return Min         



def Display(data):

    for i in range(len(data)):
        print(data[i],end="  ")

    print()    


def Accept(data,size):

    for i in range(size):
        data.append(int(input()))


def main():
    size = int(input("Number of elements"))

    data = []
     
    Accept(data,size)

    print("Elements are : ")
    Display(data)

    iRet = Minimum(data)
    print("Minimum number  : ",iRet)


if __name__ == "__main__":
    main()