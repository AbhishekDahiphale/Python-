
def DisplayR(No,start=1):
    if(start<=No):
        print(start,end="\t")
        DisplayR(No,start+1) 

def main():
    value = int(input("How many times Display : "))
    DisplayR(value)
    print("")

if __name__ == "__main__":
    main()