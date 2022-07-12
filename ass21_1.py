def DisplayAscii():
    print("Dec\t",end=" Hex\t Char\n")
    print("")
    for i in range(256):
        print(i,"\t",hex(i),"\t",chr(i))


def main():
    print("Ascii table ->-> ")
    DisplayAscii()

if __name__ == "__main__":
    main()