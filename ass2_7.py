#  5
###################
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5 
#  1 2 3 4 5 
#  1 2 3 4 5 
####################

def Pattern(No):
    for i in range(No):
        for j in range(1,No+1):
           print(j,end="  ")
        print("")    


def main():
    value = int(input("Enter the Number"))
    Pattern(value)    

if __name__ == "__main__":
    main()