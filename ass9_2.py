def ReadContent(name):

    fd = open(name,"r")

    data = fd.read()
    print("Data in the file : ",data)


def main():
    name = input("Enter the file name : ")

    ReadContent(name)


if __name__ == "__main__":
    main()