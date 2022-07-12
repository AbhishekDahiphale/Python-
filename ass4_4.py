import functools

def Accept(data,no):
    for i in range(no):
        data.append(int(input()))
        

def Display(data):
    for i in range(len(data)):
        print(data[i],end="\t") 
    print("")           


def main():
    value = int(input("how many number"))

    data = list()

    Accept(data,value)
    Display(data)

    fil = list(filter(lambda no : (no%2 == 0),data))
    print("all the even numbers from data : ",fil)

    Map = list(map(lambda no : (no*no),fil))
    print("Square of all the numbers in the fil : ",Map)

    Red = functools.reduce(lambda a,b : (a+b),Map)
    print("Addition of all Number in the map : ",Red)

   


if __name__ == "__main__":
    main()