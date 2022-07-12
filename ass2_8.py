#  5
###################
#  1 
#  1 2 
#  1 2 3  
#  1 2 3 4  
#  1 2 3 4 5 
####################

def Pattern(No):
    No= No +1
    for i in range(No):
        for j in range(1,No):
            if(i>=j):
                print(j,end="  ")  
         
        print("")    


def main():
    value = int(input("Enter the Number"))
    Pattern(value)    

if __name__ == "__main__":
    main()
    