from classes import Book

test_list = [1, 2, 3, 4, 5, 56]

for i in test_list:
    Book(i, i)

print(len(Book.all_books))
first_book = Book.all_books.pop()
print(len(Book.all_books))

Book.all_books.remove(Book.all_books[3])
print(len(Book.all_books))
