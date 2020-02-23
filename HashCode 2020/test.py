from classes import Book

test_list = [1, 2, 3, 4, 5, 56]


class Book:
    all_books = []

    def __init__(self, id, value):
        self.id = id
        self.value = value
        Book.all_books.append(self)
        self.shipped = False

    def __repr__(self):
        return f"BookID: {self.id}"


class TEST:
    all_test  = []

    def __init__(self, id, books):
        self.id = id
        self.books = books
        TEST.all_test.append(self)


for i in test_list:
    Book(i,i)
    TEST(i, Book.all_books[0])


print("BOOK PERSOPECTOVE ___________")
for i in Book.all_books:
    print(i.shipped)

print("TEST PERSOPECTOVE ___________")
for i in TEST.all_test:
    print(i.books.shipped)

TEST.all_test[0].books.shipped = True

print("TEST PERSOPECTOVE ___________")
for i in TEST.all_test:
    print(i.books.shipped)
