from functools import reduce 

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

    odd = list(filter(lambda no : (no%2 != 0),data))
    mult = reduce(lambda a,b : (a*b),odd)
    print("Product of all odd numbers : ",mult)        



if __name__ == "__main__":
    main()