class Library:
    def __init__(self,books):
        self.books = books
        self.borrowed_book = {}

    def display_books(self):
        print("Available books\n")
        if self.books:
            for book in self.books:
                print(f"-{book}")
        else:
            print("No book available..")
    def borrow_books(self,book_name,user_name):
        if book_name in self.books:
            self.books.remove(book_name)
            self.borrowed_book[book_name]=user_name
        elif book_name in self.borrowed_book:
            print(f"{book_name} have been borrowed")
        else:
            print(f"{book_name} is not available in the library")
    def return_books(self,book_name):
        if book_name in self.borrowed_book:
            user_name = self.borrowed_book.pop(book_name)
            self.books.append(book_name)
        elif book_name in self.books:
            print(f"{book_name} exixts in library")
        else:
            print(f"{book_name} exist in our library")

def main():
    print("Welcome to our library..")
    initial_books = ["Karnali blues","The alchemist","Oop","Numerical method"]
    book = Library(initial_books)
    while True:
        print("""
          Make a choice 
          1> Available books in library..
          2> Borrow a book from library..
          3> Return book you already borrowed...
          4> exit
           """)
        
        choice = int(input("Make a choice: "))
        match choice:
            case 1:
                book.display_books()
            case 2:
                name = input("Enter the name of the book: ")
                user = input("Enter the id of the user")
                book.borrow_books(name,user)
            case 3:
                name= input("Enter the name of the book: ")
                book.return_books(name)
            case 4:
                break
            case _:
                print("ERROR CASE NO NOT FOUND")

if __name__ == "__main__":
    main()

        