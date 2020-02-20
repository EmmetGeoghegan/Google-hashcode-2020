from classes import Library, Book
import time


def importdata(filename):
    with open(f"./inputdata/{filename}") as inputfile:
        lines = inputfile.readlines()
        library_count = int(lines[0].strip("\n").split(" ")[1])
        available_days = int(lines[0].strip("\n").split(" ")[2])
        book_scores = lines[1].strip("\n").split(" ")
        book_scores = [int(i) for i in book_scores]
        # Create our books
        for id, value in enumerate(book_scores):
            Book(id, value)
        lib_id = 0
        # Create librarys
        for i in range(2, 4 + library_count, 2):
            first_line = lines[i].strip("\n").split(" ")
            second_line = lines[i+1].strip("\n").split(" ")
            signup_time = int(first_line[1])
            b_per_day = int(first_line[2])
            available_books = list(set([int(i) for i in second_line]))
            Library(lib_id, signup_time, b_per_day, available_books)
            lib_id += 1
    return available_days


def get_book_location_dict():
    book_locations = dict()
    for i in Library.all_librarys:
        books = i.available_books
        for j in books:
            if j in book_locations:
                book_locations[j].append(i)
            else:
                book_locations[j] = [i]
    return book_locations


def ship_book(book):
    Book.shipped_books.append(book)
    for i in Library.all_librarys:
        i.shipped_book(book)


###################
def sign_up_library():
    sorted_libos = sorted(Library.all_librarys, key=lambda x: (-x.signup_time, len(x.available_books)))
    if Library.all_librarys:
        # input()
        chosen_libo = sorted_libos.pop()
        # print(chosen_libo)
        # print(len(Library.all_librarys))
        Library.all_librarys.remove(chosen_libo)
        # print(len(Library.all_librarys))
        Library.singing_up_libos.append(chosen_libo)
        # print(Library.singing_up_libos)
        # input()
        return chosen_libo.signup_time
    return 0


#########################
def libo_is_signed_up():
    if Library.singing_up_libos:
        libo = Library.singing_up_libos.pop()
        Library.signed_up_libos.append(libo)


##########################
def send_books(library):
    # book_locations = get_book_location_dict()
    if library.available_books:
        while True:
            if library.available_books:
                selected_book = library.available_books.pop()
                if selected_book.shipped:
                    pass
                else:
                    selected_book.shipped = True
                    break
        library.scanned_books.append(selected_book)


# filename = "b_read_on.txt"
# filename = "a_example.txt"
# filename = "c_incunabula.txt"
# filename = "d_tough_choices.txt"
# filename = "e_so_many_books.txt"
filename = "f_libraries_of_the_world.txt"


time_limit = importdata(filename)
# input()
# for i in Library.all_librarys:
#     print(i)
# input()

time_step = 0
Signing_up = False
sign_up_start_day = 0
sign_up_time = 999

while time_step < time_limit + 1:
    print("--------------")
    print(time_step, Signing_up)
    print(len(Library.all_librarys), len(Library.signed_up_libos), len(Library.singing_up_libos))
    print("--------------")
    shipping_libos = Library.signed_up_libos
    if Signing_up is False:
        sign_up_time = sign_up_library()
        # print(f"signed up libo time = {sign_up_time}")
        sign_up_start_day = time_step
        Signing_up = True
    if sign_up_start_day + sign_up_time == time_step:
        libo_is_signed_up()
        # print(f"done signeing up day: {time_step}")
        Signing_up = False

    for i in shipping_libos:
        send_books(i)
    time_step += 1


def createoutputfile(Library_class, Book_class, filename="sub.txt"):
    timestamp = str(time.time()).replace(".", "")
    with open(f"./submission/{timestamp}{filename}", "w+") as outputfile:
        outputfile.write(str(len(Library_class.signed_up_libos))+"\n")
        for i in Library_class.signed_up_libos:
            outputfile.write(f"{i.id} {len(i.scanned_books)}"+"\n")
            outputfile.write(" ".join([str(i.id) for i in i.scanned_books])+"\n")


createoutputfile(Library, Book, filename)
