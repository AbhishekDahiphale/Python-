def DisplayEven(no):
    i=0
    j=1
    while(i!=no):
        if((j%2)==0):
            print(j,end="  ")
            i=i+1
        j=j+1  

    print("")      

def main():
    No = int(input("Enter the Numebr"))

    DisplayEven(No)
    



if __name__ == "__main__":
    main()