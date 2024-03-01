import datetime

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        while True:
            publication_year = input("Enter publication year: ")
            current_year = datetime.datetime.now().year

            if publication_year.isdigit() and 0 < int(publication_year) <= current_year:
                break
            else:
                print("Invalid year. Please enter a valid publication year.")

        new_book = Book(title, author, int(publication_year))
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def view_all_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("List of Books:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")

    def search_book(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print("Found Books:")
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
        else:
            print(f"No books found with the title '{title}'.")

# Example usage
if __name__ == "__main__":
    book_manager = BookManager()

    while True:
        print("\nOptions:")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Search for a book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            book_manager.add_book(title, author)
        elif choice == "2":
            book_manager.view_all_books()
        elif choice == "3":
            search_title = input("Enter the title of the book to search: ")
            book_manager.search_book(search_title)
        elif choice == "4":
            print("Exiting the book manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
