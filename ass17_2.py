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

    even = list(filter(lambda no : (no%2 == 0),data))
    odd = list(filter(lambda no : (no%2 != 0),data))
    print("Difference between even and odd elements : ",(len(even) - len(odd)))



if __name__ == "__main__":
    main()