def Addition(data):
    isum = 0
    for i in range(len(data)):
        isum = isum + data[i]

    return isum    



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

    iRet = Addition(data)
    print("Addition of all numbers are : ",iRet)


if __name__ == "__main__":
    main()