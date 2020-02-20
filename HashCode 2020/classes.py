
class Book:
    all_books = []

    def __init__(self, id, value):
        self.id = id
        self.value = value
        Book.all_books.append(self)
        self.shipped = False

    def __repr__(self):
        # return f"BookID: {self.id} Book_Val: {self.value}"
        return f"BookID: {self.id}"


class Library:
    all_librarys = []
    singing_up_libos = []
    signed_up_libos = []

    def __init__(self, id, signup_time, b_per_day, available_books):
        self.id = id
        self.signup_time = signup_time
        self.b_per_day = b_per_day
        self.available_books = self.create_books(available_books)
        self.scanned_books = []
        self.useful_books = []

        Library.all_librarys.append(self)

    def create_books(self, booklist):
        output = []
        for i in booklist:
            output.append(Book.all_books[i])
        return output

    def __repr__(self):
        return str(self.id)
