def Display(No):
    for i in range(No):
        print("*",end="  ")
    print("")    

def main():
    No = int(input("How many times Display"))
    Display(No)



if __name__ == "__main__":
    main()