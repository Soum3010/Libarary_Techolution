class User:
    def __init__(self, user_id, name, pin):
        self.user_id = user_id
        self.name = name
        self.pin = pin
        self.books_issued = []
    
    def to_json(self):
        return {"user_id":self.user_id,"name":self.name,"pin":self.pin,"books_issued":self.books_issued}

class Book:
    def __init__(self, title, author, isbn,copies=1):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = copies

    def to_json(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "copies": self.copies,
        }
        