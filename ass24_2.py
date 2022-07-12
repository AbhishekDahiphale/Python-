from StringX import CntCharFreq

def main():
    String = input("Enter the string : ")
    ch = input("Enter the chracter : ")[0]
    
    Ret = CntCharFreq(String,ch)
    print("Frequrency  of "+ch+" int the given string are : ",Ret)    

if __name__ == "__main__":
    main()