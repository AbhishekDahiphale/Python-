
def Accept(data,No):
    for i in range(No):
        data.append(int(input())) 

def Display(data):
    for i in range(len(data)):
        print(data[i],end="\t")
    print("")

def sumdigit(no):
    sum = 0 
    while(no!=0):
        digit = int(no%10)
        sum = sum + digit
        no = int(no/10)

    return sum    

         

def main():
    value = int(input("How many numbers : "))
     
    data = list()

    Accept(data,value)
    Display(data)

    Ret = list(map(sumdigit,data))
    print("sum of all digits  : ",Ret)       



if __name__ == "__main__":
    main()