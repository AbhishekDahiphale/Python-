#  5
###################
#  * * * * *
#  * * * * 
#  * * * 
#  * * 
#  *   
####################

def Pattern(No):
    for i in range(No):
        for j in range(No):
            if(i<=j):
                print("*",end="  ")
        print("")    


def main():
    value = int(input("Enter the Number"))
    Pattern(value)    

if __name__ == "__main__":
    main()