from StringX import Diff

def main():
    String  = input("Enter the string : ")

    Ret = Diff(String)
    print("Difference between small and capital letters in the string : ",Ret)

if __name__ == "__main__":
    main()