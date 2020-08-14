
from book import Book
from bookitem import Bookitem

class user:
    def __init__(self, name, age, location, aadhar_id):
        self.name = name
        self.age = age
        self.location = location
        self.aadhar_id = aadhar_id


    def __repr__(self):
        return self.name + "\n" + self.location

    #functions common for both student and librarian

    def displayAllbooks(self):
        if len(Book.Books_list) == 0:
            print("no books available")
        else:
            for book in Book.Books_list:
                print("{} by {} in {} is available".format(book.title, book.author, book.genre))


    def showReservedbooks(self):
        if len(Bookitem.reserved_books) >= 1:
            for book in Bookitem.reserved_books:
                print ("{} by {} is reserved currently".format(book.title, book.author))
        else:
            print ("no books are reserved currently")

    def searchbyTitle(title):
        for book in Book.Books_list:
            if book.title == title:
                print("The book {} is available".format(book.title))
                break
        else:
            print("Sorry.. no books are available by this title!")

    def searchbyAuthor(author):
        for book in Book.Books_list:
            if book.author == author:
                print("Books by author {} are {}".format(book.author, book.title))
                break
        else:
            print("No book by this author")

    def searchbyGenre(genre):
        for book in Book.Books_list:
            if book.genre == genre:
                print ("Book in {} are {}".format(genre, book.title))
        else:
            print("No book in this genre")

    def searchbyPublisher(publisher):
        for book in Book.Books_list:
            if book.publisher == publisher:
                print ("books by {} are {}".format(publisher, book.title))
        else:
            print("No book by this publisher")