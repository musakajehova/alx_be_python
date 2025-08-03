#book library

class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

    def check_out(self):
        if self._is_checked_out == False:
            self._is_checked_out = True
            print("Book has been succefully checked out \n")
        else:
            return False
        
    def returning(self):
            self._is_checked_out = False
    
    def available(self):
        if self._is_checked_out == False:
            return not self._is_checked_out
        else:
            return False
    
    def display(self):
        print(f"{self.title} by {self.author}   {self._is_checked_out}")


class Library: 

    def __init__(self):
        self._books = []
    
    def add_book(self, book_add: Book):
        self._books.append(book_add)
    
    def check_out_book(self, title):
        for x in self._books:
            if (title == x.title) and (x.available() == True):
                x.check_out()
                break
            else :
                print("No such book exists")

    
    def return_book(self, title):
        for x in self._books:
            if (title == x.title) and (x.available() == False):
                x.returning()
                break
            else :
                print("No such book exists")

    def list_available_books(self):
        """Prints out the books"""
        for i in self._books:
            if i.available() == True:
                i.display()
        print("\n")