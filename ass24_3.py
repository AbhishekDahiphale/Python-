from StringX import firsOcc

def main():
    String = input("Enter the string : ")
    ch = input("Enter the chracter : ")[0]
    
    Ret = firsOcc(String,ch)
    print("First Occur the charcter at ",Ret," Index")    

if __name__ == "__main__":
    main()