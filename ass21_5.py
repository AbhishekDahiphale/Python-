def Display(ch):
    print("Decimal     : ",ord(ch))
    print("Octal       : ",oct(ord(ch)))
    print("Hexadecimal : ",hex(ord(ch)))

def main():
    value = input("Enter the chracter : ")[0]

    Display(value)

if __name__ == "__main__":
    main()