# Simple Library Management System

def add_book(library):
    """Add a new book to the library with validation."""
    while True:  # Loop to ensure valid input
        title = input("Enter book title: ").strip()
        if not title:
            print("Invalid input. Title cannot be empty. Please try again.")
            continue  # Prompt the user again

        author = input("Enter book author: ").strip()
        if not author:
            print("Invalid input. Author cannot be empty. Please try again.")
            continue  # Prompt the user again

        # If both inputs are valid
        book = {"title": title, "author": author, "available": True}
        library.append(book)
        print("Book added successfully.")
        break  # Exit the loop after successful addition


def search_book(library):
    """Search for a book by title or author."""
    keyword = input("Enter search keyword (title or author): ").strip()
    results = [book for book in library if
               keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]

    if results:
        print("\nSearch Results:")
        for book in results:
            status = "Available" if book["available"] else "Borrowed"
            print(f"Title: {book['title']}, Author: {book['author']}, Status: {status}")
    else:
        print("No matching books found.")
    print()


def borrow_book(library):
    """Borrow a book if it is available."""
    title = input("Enter the title of the book to borrow: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                print(f"You have successfully borrowed '{book['title']}'.")
                return
            else:
                print(f"Sorry, the book '{book['title']}' is currently borrowed.")
                return
    print(f"Book '{title}' not found in the library.")


def return_book(library):
    """Return a borrowed book."""
    title = input("Enter the title of the book to return: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            if not book["available"]:
                book["available"] = True
                print(f"Thank you for returning '{book['title']}'.")
                return
            else:
                print(f"The book '{book['title']}' was not borrowed.")
                return
    print(f"Book '{title}' not found in the library.")


def display_menu():
    """Display the main menu."""
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")


def main_menu():
    """Main program loop."""
    library = []  # Initialize an empty library list
    while True:
        display_menu()
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
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Run the program
if __name__ == "__main__":
    main_menu()
