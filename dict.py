class address:
    def __init__(self) :
        self.__book = []
        
    def add_book(self, name, email):
        for books in self.__book:
            if name == books["name"]:
                print("Contact already exist")
                return
        else:
            self.__book.append({"name": name, "email": email})
        
    def add_book2(self, name, email):
        
        if not any(list(filter(lambda a: a["name"] == name, self.__book))):
            self.__book.append({"name": name, "email": email})
        else:
            print("Contact not found")
    def remove_book(self, name):
        for books in self.__book:
            if name == books["name"]:
                self.__book.remove(books)
                return
        else:
            print("Contact not found")
    def list_books(self):
        return self.__book

a = address()
a.add_book("Dexter", "dexteringuito@gmail.com")
a.add_book("inguito", "inguito@gmail.com")
a.add_book("hulahoop", "hulaloop@hdw.com")
a.add_book("hulahoop", "hulaloop@hdw.com")
a.add_book("hulahoop", "hulaloop@hdw.com")
print(a.list_books())
a.remove_book("ohaha")
a.remove_book("hulahoop")
print(a.list_books())
        