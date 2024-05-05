from models import Book
from storage import read_storage,write_storage
import traceback

class BookManagement(Book):
    def __init__(self):
        super().__init__(isbn=None, title=None, author=None, copies=0)
        self.book_id_generator = self.generate_book_id()

    def generate_book_id(self):
        try:
            data = read_storage("utils.json")
            counter = data.get('book_counter', 0)

            while True:
                counter += 1
                data['book_counter'] = counter
                write_storage(data, 'utils.json')
                yield f"B_{counter}"
        except Exception as e:
            print(f"Error in generating ISBN: {str(e)}")
    
    def add_book(self, title, author,copies=1):
        book_id = next(self.book_id_generator)
        new_book = Book(title, author,book_id,copies).to_json()

        try:
            data = read_storage("books.json")  
            data[book_id] = new_book
            write_storage(data, "books.json")
            print("Book added successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print(traceback.format_exc())

    def list_books(self):
        try:
            data = read_storage("books.json")
            for isbn, book_info in data.items():
                print(f"ISBN: {isbn}")
                print(f"Title: {book_info['title']}")
                print(f"Author: {book_info['author']}")
                print(f"Copies_Available: {book_info['copies']}")
                print()  # Print an empty line for spacing
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    def search_books(self, attribute, value):
        try:
            data = read_storage("books.json")
            found_books = []
            for book_id, book_info in data.items():
                if str(book_info.get(attribute, '')).lower() == str(value).lower():
                    found_books.append((book_id, book_info))
            
            if found_books:
                print("Matching books found:")
                for book_id, book_info in found_books:
                    print(f"ISBN: {book_info['isbn']}")
                    print(f"Title: {book_info['title']}")
                    print(f"Author: {book_info['author']}")
                    print(f"Copies Available:{book_info['copies']}")
                    print()  # Print an empty line for spacing
            else:
                print("No matching books found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    def delete_book(self, isbn):
        try:
            data = read_storage("books.json")
            if isbn in data:
                del data[isbn]
                write_storage(data, "books.json")  # Write updated book data
                print("Book deleted successfully.")
            else:
                print("Book ID not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    def update_book(self, isbn, new_title=None, new_author=None,copies=0):
        try:
            data = read_storage("books.json")
            if isbn in data:
                if new_title:
                    data[isbn]['title'] = new_title
                if new_author:
                    data[isbn]['author'] = new_author
                if copies:
                    data[isbn]['copies'] = copies
                write_storage(data, "books.json")  # Write updated book data
                print("Book updated successfully.")
            else:
                print("Book ID not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")