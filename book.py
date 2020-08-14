

class Book:
    Book_item =[]
    Books_list = []
    total_books_available = 0
    def __init__(self, title, author, genre, publisher):
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        Book.Books_list.append(self)
