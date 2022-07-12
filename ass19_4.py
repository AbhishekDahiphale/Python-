
def Accept(data,No):
    for i in range(No):
        data.append(int(input())) 

def Display(data):
    for i in range(len(data)):
        print(data[i],end="\t")
    print("")

def Chk3digit(no):
    cnt = 0 
    while(no!=0):
        digit = int(no%10)
        cnt +=1
        no = int(no/10)

    if(cnt == 3 ):
        return True
    else:
        return False     

def main():
    value = int(input("How many numbers : "))
     
    data = list()

    Accept(data,value)
    Display(data)

    Ret = list(filter(Chk3digit,data))
    print("Elements which have three digits : ",Ret)       



if __name__ == "__main__":
    main()