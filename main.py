from book import BookManagement as book_manager
from user import UserManagement as user_manager
from check import CheckManagement as check_manager

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    print("<-----------------------Performing Operation --------------------------->")
    return choice.strip()

def add_book():
    print("\nAdd Book")
    title = input("Enter title: ")
    author = input("Enter author: ")
    copies = int(input("Enter Number of Copies available: "))
    book_manager().add_book(title, author, copies)

def list_books():
    print("\nList Books")
    book_manager().list_books()

def add_user():
    print("\nAdd User")
    name = input("Enter user name: ")
    user_manager().add_user(name)
    print("User added successfully.")

def checkout_book():
    print("\nCheckout Book")
    user_id = input("Enter user ID: ")
    if user_manager.is_valid(user_id):
        isbn = input("Enter ISBN of the book to checkout: ")
        pincode = input("Enter Pincode: ")
        check_manager().check_out_book(isbn=isbn,user_id=user_id,pincode=pincode)
    else:
        print("Create an Account First or give valid User_id")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            add_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            add_user()
        elif choice == '4':
            checkout_book()
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
        print("<-----------------------Operation Completed--------------------------->")

if __name__ == "__main__":
    main()