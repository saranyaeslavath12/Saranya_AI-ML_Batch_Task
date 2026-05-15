def add_book(catalog,book_id,title,author,year):
    if book_id in catalog:
        print("Book ID already exists.")
    else:
        catalog[book_id] = (title, author , year)
        print("Book added successfully.")

def borrow_book(catalog,borrowed_books,book_id):
    if book_id not in catalog:
        print("Book ID does not exist.")

    elif book_id in borrowed_books:
        print("Book is already borrowed.")
        
    else:
        borrowed_books.append(book_id)
        print("Book borrowed successfully.")

def return_book(borrowed_books,book_id):
    if book_id not in borrowed_books:
        print("Book was not borrowed.")
    else:
        borrowed_books.remove(book_id)
        print("Book returned successfully.")

def register_member(members,member_id):
    if member_id in members:
        print("Member ID already exists.")
    else:
        members.add(member_id)
        print("Member registered successfully.")
    
def show_available(catalog,borrowed_books):
    available_books = {book_id: details for book_id, details in catalog.items() if book_id not in borrowed_books}
    print("Available books:")
    for book_id, (title, author, year) in available_books.items():
        print(f"  {book_id}: {title} by {author} ({year})")

def main():
    catalog = {}
    borrowed_books = []
    members = set()

    add_book(catalog, 101, "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    add_book(catalog, 102, "To Kill a Mockingbird", "Harper Lee", 1960)
    add_book(catalog, 101, "1984", "George Orwell", 1949) # Duplicate ID
    add_book(catalog, 104, "Atomic Habits", "James Clear", 2018)


    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 101)# Duplicate ID

    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 101) # Already borrowed
    borrow_book(catalog, borrowed_books, 103)  # Non-existent book

    return_book(borrowed_books, 101)
    return_book(borrowed_books, 101)  # Not borrowed

    show_available(catalog, borrowed_books)
if __name__ == "__main__":
    main()

