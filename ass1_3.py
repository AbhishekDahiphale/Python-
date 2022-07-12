def Addition(No1,No2):
    return (No1+No2)

def main():
    No1 = int(input("Enter the first Number"))
    No2 = int(input("Enter the Second Number"))

    Ret = Addition(No1,No2)
    print("Addition is : ",Ret)    


if __name__ == "__main__":
    main()