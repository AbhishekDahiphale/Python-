def Display(No):
    for i in range(No,0,-1):
        print(i)

def main():
    No = int(input("How many times Display"))
    Display(No)



if __name__ == "__main__":
    main()