class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.BookName = Name
        self.BookAuthor = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.BookName," By ",self.BookAuthor)
        print("Number of books are :  : ",self.NoOfBooks)   

def main():
    Name = input("Enter the Name of Book : ")
    Author = input("Enter the Author Name : ")

    obj1 = BookStore(Name,Author)
    obj1.Display()

    Name = input("Enter the Name of Book : ")
    Author = input("Enter the Author Name : ")

    obj1 = BookStore(Name,Author)
    obj1.Display()


if __name__ == "__main__":
    main()