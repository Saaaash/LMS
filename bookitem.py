
class Bookitem:
    reserved_books = []                           #has all books taken by students
    activemembers = {}

    def addtoreserved(title):    #adds book to reserved list
        Bookitem.reserved_books.append(title)


    def __init__(self, book, isbn, rack):
        self.book = book
        self.isbn = isbn
        self.rack = rack

    def updateActivemembers(self, name, roll_no, title, isbn, days):   #contains user and book & isbn details
        self.activemembers["Name"] = name
        self.activemembers["Roll no"] = roll_no
        self.activemembers["title"] = title
        self.activemembers["isbn"] = isbn
        self.activemembers["Days"] = days


    def removefromReservedlist(title):
        Bookitem.reserved_books.remove(title)

    def clearActivemember(self):
        self.activemembers.clear()


