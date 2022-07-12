from StringX import ChkVowel

def main():
    String  = input("Enter the string : ")

    Ret = ChkVowel(String)
    if(Ret == True):
        print("Vowel Present ")
    else:
        print("Vowel NOT Present!!! ")    

if __name__ == "__main__":
    main()