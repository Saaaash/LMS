from user import user
class Quicksearch:
    def quicksearch(self):
        print ("welcome to Quick Search menu \n How you want to Search your book?")
        print ("1. By Book Title \n 2. By Author \n 3. By Publisher \n 4. By genre")
        choice = int(input("enter your choice:"))
        if choice == 1:
            name = input("Please Enter book name: ")
            user.searchbyTitle(name)
        elif choice == 2:
            author = input("please enter author name: ")
            user.searchbyAuthor(author)
        elif choice == 3:
            publisher = input("Enter publisher name: ")
            user.searchbyPublisher(publisher)
        elif choice == 4:
            genre = input("enter genre of your preference: ")
            user.searchbyGenre(genre)
        else:
            print (" Please try Again !! ")


