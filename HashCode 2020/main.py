from classes import Library, Book
from tqdm import tqdm


# Import all data from the input file
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


# Book lookup tables to find what librarys a book is in
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


# Choose a library to sign up
def sign_up_library():
    sorted_libos = sorted(Library.all_librarys, key=lambda x: (-x.signup_time, len(x.available_books)))
    if Library.all_librarys:
        chosen_libo = sorted_libos.pop()
        Library.all_librarys.remove(chosen_libo)
        Library.signing_up_libos.append(chosen_libo)
        return chosen_libo.signup_time
    return 0


# Library has finished signing up. Add it to the singed up librarys
def libo_is_signed_up():
    if Library.signing_up_libos:
        libo = Library.signing_up_libos.pop()
        Library.signed_up_libos.append(libo)


# Send a book to Google
def send_books(library):
    # book_locations = get_book_location_dict()
    if library.available_books:
        loop = True
        sorted_books = sorted(library.available_books, key=lambda x: x.value)
        while loop is True:
            if library.available_books:
                if not sorted_books:
                    break
                else:
                    selected_book = sorted_books.pop()
                if selected_book.shipped is True:
                    pass
                else:
                    selected_book.shipped = True
                    loop = False
        library.scanned_books.append(selected_book)


def algorithm(filename):
    time_limit = importdata(filename)
    time_step = 0
    Signing_up = False
    sign_up_start_day = 0
    sign_up_time = 999

    pbar = tqdm(total=time_limit)
    while time_step < time_limit + 1:
        shipping_libos = Library.signed_up_libos
        if Signing_up is False:
            sign_up_time = sign_up_library()
            sign_up_start_day = time_step
            Signing_up = True
        if sign_up_start_day + sign_up_time == time_step:
            libo_is_signed_up()
            Signing_up = False

        for i in shipping_libos:
            send_books(i)
        time_step += 1
        pbar.update(1)
    pbar.close()
    createoutputfile(Library, Book, filename, scoring_func())


def createoutputfile(Library_class, Book_class, filename, score):
    with open(f"./submission/{score}__{filename.split('_')[0]}_sub.txt", "w+") as outputfile:
        outputfile.write(str(len(Library_class.signed_up_libos))+"\n")
        for i in Library_class.signed_up_libos:
            outputfile.write(f"{i.id} {len(i.scanned_books)}"+"\n")
            outputfile.write(" ".join([str(i.id) for i in i.scanned_books])+"\n")


def scoring_func():
    return 0
    # TODO make a scoring function to evaluate on the fly


def main():
    all_files = []
    all_files.append("a_example.txt")
    all_files.append("b_read_on.txt")
    all_files.append("c_incunabula.txt")
    all_files.append("d_tough_choices.txt")
    all_files.append("e_so_many_books.txt")
    all_files.append("f_libraries_of_the_world.txt")
    for filename in all_files:
        print(f"Running {filename}")
        algorithm(filename)
        print("Done")
        print("---------------------------------")
        wipe_environment()


def wipe_environment():
    Library.all_librarys = []
    Library.unsigned_libos = []
    Library.signing_up_libos = []
    Library.signed_up_libos = []
    Book.all_books = []
    Book.unshipped_books = []
    Book.shipped_books = []


if __name__ == '__main__':
    main()
