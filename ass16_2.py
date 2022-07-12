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

    Ret = list(filter(lambda no : (no%5 == 0),data))
    print(" elements which are divisible by 5 : ",Ret)



if __name__ == "__main__":
    main()