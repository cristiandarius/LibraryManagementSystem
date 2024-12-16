def add_book(library):
    print("\n--- Add a New Book ---")
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    if title and author:
        book = {"title": title, "author": author, "available": True}
        library.append(book)
        print("Book added successfully.")
    else:
        print("Invalid input. Title and Author cannot be empty.")

def search_book(library):
    print("\n--- Search for a Book ---")
    keyword = input("Enter search keyword (title or author): ").strip()
    matches = [book for book in library if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]
    if matches:
        print("Matching books:")
        for book in matches:
            print(f"Title: {book['title']}, Author: {book['author']}, Available: {'Yes' if book['available'] else 'No'}")
    else:
        print("No matching books found.")

def borrow_book(library):
    print("\n--- Borrow a Book ---")
    title = input("Enter the title of the book to borrow: ").strip()
    for book in library:
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            print("Book borrowed successfully.")
            return
    print("Book not available or already borrowed.")

def return_book(library):
    print("\n--- Return a Book ---")
    title = input("Enter the title of the book to return: ").strip()
    for book in library:
        if book["title"].lower() == title.lower() and not book["available"]:
            book["available"] = True
            print("Book returned successfully.")
            return
    print("Book not found or not borrowed.")

def display_books(library):
    print("\n--- Display All Books ---")
    if library:
        for index, book in enumerate(library, start=1):
            print(f"{index}. Title: {book['title']}, Author: {book['author']}, Available: {'Yes' if book['available'] else 'No'}")
    else:
        print("The library is currently empty.")

def main_menu():
    # Predefined list of books
    library = [
        {"title": "Python Programming", "author": "John Doe", "available": True},
        {"title": "Data Science Basics", "author": "Jane Smith", "available": True},
        {"title": "Artificial Intelligence", "author": "Alan Turing", "available": True},
        {"title": "Clean Code", "author": "Robert C. Martin", "available": True},
    ]
    
    print("Welcome to the Library Management System!")
    print("Manage your library with ease.")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_book(library)
            elif choice == 2:
                search_book(library)
            elif choice == 3:
                borrow_book(library)
            elif choice == 4:
                return_book(library)
            elif choice == 5:
                display_books(library)
            elif choice == 6:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
