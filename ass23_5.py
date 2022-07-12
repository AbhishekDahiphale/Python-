from StringX import CntWhite

def main():
    String = input("Enter the string : ")
    
    Ret = CntWhite(String)
    print(String+" Number of white spaces are  : ",Ret)

if __name__ == "__main__":
    main()