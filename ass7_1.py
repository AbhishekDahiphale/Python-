
def DisplayR(No):
    if(No!=0):
        print("*",end="\t")
        DisplayR(No-1)    

def main():
    value = int(input("How many times Display : "))
    DisplayR(value)
    print("")

if __name__ == "__main__":
    main()