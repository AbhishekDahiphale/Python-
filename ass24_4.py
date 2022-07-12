from StringX import lastOcc

def main():
    String = input("Enter the string : ")
    ch = input("Enter the chracter : ")[0]
    
    Ret = lastOcc(String,ch)
    print("Last Occur the charcter at ",Ret," Position")    

if __name__ == "__main__":
    main()