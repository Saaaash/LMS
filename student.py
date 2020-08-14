
from user import user
from book import Book
from bookitem import Bookitem
from duecalculation import Duecalculation

class Student:
    student_list = []
    def __init__(self, name, age,  location, aadhar_id, roll_no):
        user.__init__(name, age,  location, aadhar_id)
        self.roll_no = roll_no
        self.my_bag = []
        self.student_list.append(self)

    def __repr__(self):
        return "\n" + self.roll_no

    def getBook(self, name, roll_no, title, isbn, days):
        if len(self.my_bag) >= 1:
            for books in Book.Books_list:
                if books.title == title:
                    Book.Books_list.pop()
                    Book.total_books_available -= 1
                    Bookitem.addtoreserved(title)
                    Bookitem.updateActivemembers(name, roll_no, title, isbn, days)
                    self.my_bag.append(title)
                    print("you can get your book at {}".format(books.rack))
                break
            else:
                print ("no such books found")
        if len(self.my_bag) <= 5:
            print ("you cant get more than 4 books at a time. please return a book to get this book. Thank you")
        else:
            print ("enter valid choice")

    def returnBook(self, book_to_be_returned, days):
        if len(self.my_bag) == 0:
            print ("no books to return")
        else:
            for books in self.my_bag:
                if books.title == book_to_be_returned:
                    print ("you can return the book now")
                    Bookitem.removefromReservedlist(book_to_be_returned)
                    Bookitem.clearActivemember(book_to_be_returned)
                    Book.total_books_available += 1
                    Duecalculation.calculateDue(days)

    def viewMybooks(self):
        if len(self.my_bag) >= 1:
            for books in self.my_bag:
                print ("{} are in your bag".format(books.title))
                break
        else:
            print ("no books in your bag")