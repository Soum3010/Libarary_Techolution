from datetime import datetime, timedelta
import json
from user import UserManagement
from storage import read_storage,write_storage

class CheckManagement:
    user_management = UserManagement()
    def __init__(self):
        pass

    @user_management.authenticate_user
    def check_out_book(self, isbn, user_id, pincode):
        try:
            user_data = read_storage("users.json")
            if user_id in user_data:
                user_info = user_data[user_id]
                if len(user_info['books_issued']) < 5:  # Check if maximum limit is reached
                    book_data = read_storage("books.json")
                    if isbn in book_data:
                        book_info = book_data[isbn]
                        if book_info['copies'] > 0:
                            book_info['copies'] -= 1
                            transaction_id = f'T_{datetime.now().strftime("%Y%m%d%H%M%S")}'
                            due_date = datetime.now() + timedelta(days=14)
                            transaction_data = {
                                "transaction_id": transaction_id,
                                "user_id": user_id,
                                "isbn": isbn,
                                "issue_date": datetime.now().strftime("%Y-%m-%d"),
                                "due_date": due_date.strftime("%Y-%m-%d"),
                            }
                            
                            transactions = read_storage("transactions.json")
                            transactions[transaction_id] = transaction_data
                            user_info['books_issued'].append(isbn)  # Update user's books issued
                            
                            write_storage(transaction_data,"transactions.json")
                            write_storage(book_data, "books.json")  # Write updated book data
                            write_storage(user_data, "users.json")  # Write updated user data
                            print("Book checked out successfully.")
                        else:
                            print("No copies available for this book.")
                    else:
                        print("Book not found.")
                else:
                    print("Maximum limit reached for issuing books. Please return some books first.")
            else:
                print("User not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")