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

    No = int(input("Enter the number to count frequency : ")) 
    Ret = list(filter(lambda no : (no == No),data))
    print("Frequency of given number : ",len(Ret))    



if __name__ == "__main__":
    main()