def convert(Ch):
    if(Ch >= 'A' and Ch <= 'Z'):
        Ch = chr(ord(Ch)+32)
        print("Conveted character : ",Ch)
    elif(Ch >= 'a' and Ch <= 'z'):
        Ch = chr(ord(Ch)-32)
        print("Converted charcter : ",Ch)
    else:
        print("I is not alphabet!!")    


def main():
    value = input("Enter the chracter : ")[0]

    convert(value)


if __name__ == "__main__":
    main()