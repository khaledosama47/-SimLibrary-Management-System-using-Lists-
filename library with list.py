#task:1
#خالد أسامه عبدالعزيز خليفه
#سكشن الاحد
library = []  
while True:
    print("\nLIBRARY MANAGEMENT SYSTEM")
    print("1- Add a book")
    print("2- View all books")
    print("3- Delete a book")
    print("4- Search for a book")
    print("5- Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        book = input("Enter the book title: ").strip()
        if book:
            library.append(book)
            print(f'"{book}" has been added to the library.')
        else:
            print("Book title cannot be empty.")

    elif choice == "2":
        if library:
            print("\nLibrary Collection:")
            for index, book in enumerate(library, start=1):
                print(f"{index}. {book}")
        else:
            print("The library is empty.")

    elif choice == "3":
        if library:
            book_to_delete = input("Enter the book title to remove: ").strip()
            if book_to_delete in library:
                library.remove(book_to_delete)
                print(f'"{book_to_delete}" has been removed from the library.')
            else:
                print("Book not found in the library.")
        else:
            print("No books available to delete.")

    elif choice == "4":
        search_query = input("Enter the book title to search for: ").strip()
        matching_books = [book for book in library if search_query.lower() in book.lower()]
        if matching_books:
            print("\nMatching books:")
            for book in matching_books:
                print(f"- {book}")
        else:
            print("No matching books found.")

    elif choice == "5":
        print("Thanks for using the Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
