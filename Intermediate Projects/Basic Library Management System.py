class Book:
    # Store title, author, isbn, availablity.

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True       # Since it was stored now, Book will definitely be available
        Library.books.append({"Title": self.title,
                              "Author": self.author, 
                              "ISBN": self.isbn, 
                              "Availability": self.available})
        print("-" * 60)
        print(f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"Isbn: {self.isbn}")
        for book in Library.books:
            if book["Availability"] == True:
                print("Available: Yes")
            else:
                print("Availability: No")

    def book_availability(self):
        print("-" * 60)
        for book in Library.books:
            if book["Availability"] == True:
                print(f"{book['Title']} is available.")
            else:
                print(f"{book['Title']} is not available.")


class Members:
    def __init__(self, name, member_id, borrowed_books=0):
        self.borrowed_books = borrowed_books
        Library.registered_members.append({"Name": name,
                                           "Member ID": member_id,
                                           "Borrowed Books": borrowed_books})

    def borrow_book(self, check_name, check_member_id, book_to_borrow):
        for member in Library.registered_members:
            if check_name == member["Name"] and check_member_id == member["Member ID"]:
                for book in Library.books:
                    if book_to_borrow == book["Title"]:
                        if book["Availability"]:
                            book["Availability"] = False
                            member["Borrowed Books"] +=1
                            print(f"✅ {check_name} borrowed '{book_to_borrow}'")
                            return
                        else:
                            print(f"{book_to_borrow} is not available.")
                            return
                print(f"{book_to_borrow} is not found in the library.")
                return
        print("Details not found, Please Register before trying to borrow.")

    def all_members(self):
        print("-" * 60)
        for index, member in enumerate(Library.registered_members):
            print(f"{index}. Name: {member['Name']}, ID: {member['Member ID']}, Borrowed Books: {member['Borrowed Books']}")

    def return_book(self, check_name, check_member_id, book_to_return):
        for book in Library.books:
            if book_to_return == book["Title"] and book["Availability"] == False:
                for member in Library.registered_members:
                    if check_name == member["Name"] and check_member_id == member["Member ID"]:
                        book["Availability"] = True
                        member["Borrowed Books"] -=1
                        print(f"{check_name} has returned {book_to_return} and still with {member['Borrowed Books']} books.")
                        return
                print("Member not found.")
                return
        print("Book not found or is already available.")


class Library:
    books = []
    registered_members = []
