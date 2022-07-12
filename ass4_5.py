import functools

def Accept(data,no):
    for i in range(no):
        data.append(int(input()))
        

def Display(data):
    for i in range(len(data)):
        print(data[i],end="\t") 
    print("")   

def ChkPrime(no):
    flag = True
    for i in range(2,int(no/2)+1):
        if(no%i == 0):
            flag = False               

    if(flag == True):
        return no

def Max(no1,no2):
    if(no1 < no2):
        return no2
    else:
        return no1    
                  
    

def main():
    value = int(input("how many number"))

    data = list()

    Accept(data,value)
    Display(data)

    fil = list(filter(ChkPrime,data))
    print("all the prime numbers from data : ",fil)

    Map = list(map(lambda no : (no*2),fil))
    print("Multiply each number by 2 in the fil : ",Map)

    Red = functools.reduce(lambda a,b : Max(a,b),Map)
    print("Maximum number is  : ",Red)

   


if __name__ == "__main__":
    main()