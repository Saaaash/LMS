from user import user
from book import Book
from bookitem import Bookitem
from student import Student

class Librarian:
    def __init__(self, name, age,  location, aadhar_id, employee_id):
        user.__init__(name, age,  location, aadhar_id)
        self.employee_id = employee_id

    def __repr__(self):
        return "\n" + self.employee_id

    def addBook(self, title, author, genre, publisher):
        b = Book(title, author, genre, publisher)
        Book.Books_list.append(b)
        print ("{} has been added to library successfully!".format(title))


    def addBookitem(self, title, isbn, rack):
        for book in Book.Books_list:
            if book.title == title:
                Book.Book_item.append(title, isbn, rack)
                print("The book {} of isbn {} is added to bookitem".format(title, isbn))

    def removeBook(book_to_be_removed):
        for book in Book.Books_list:
            if book.title == book_to_be_removed:
                Book.Books_list.remove(book_to_be_removed)
        else:
            print("no such books found")


    def removeBookitem(remove_bookitem):
        if len(Book.Book_item) >= 1:
            for book in Book.Books_list:
                if book.title == remove_bookitem:
                    Book.Books_list.remove(remove_bookitem)
                    break
        else:
            print("no such books found")

    def showMembers(self):
        if len(Student.student_list) >= 1:
            for students in Student.student_list:
                print ("{} of {}".format(students.name, students.location))
        else:
            print("no students are enrolled")

    def viewActivemembers(self):
        print Bookitem.activemembers.items()
