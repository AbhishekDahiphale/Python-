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

    fil = list(filter(lambda no : (no <= 90 and no >= 70 ),data))
    print("Using filter data is : ",fil)

    Map = list(map(lambda no : (no + 10),fil))
    print("using map  : ",Map)

    Red = functools.reduce(lambda a, b : (a*b),Map)
    print("product of all numbers in the map : ",Red)

   


if __name__ == "__main__":
    main()