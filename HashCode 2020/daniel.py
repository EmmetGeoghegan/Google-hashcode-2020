def importdata(filename):
    with open(f"./HashCode 2020/inputdata/{filename}", "r") as inputfile:
        lines = inputfile.readlines()
        #even readlines
        count = 0
        newline = lines[0].strip("\n").split(" ")
        #total number of books
        number_books = newline[0]
        #total number of libraries
        number_libraries = newline[1]
        #total number of days
        number_days = newline[2]
        newline = lines[1].strip("\n").split(" ")
        #scores of individual books
        book_scores = newline[1]
        library_data = []

        for i in range(2, int(number_libraries), 2):
            library = []
            count += 1
            library_id = count
            #book_ids are on all the odd lines
            library_books_ids =  lines[i+1].strip("\n").split(" ")
            #splits even lines into the three values to be extracted
            even_lines = lines[i].strip("\n").split(" ")
            #number of books in library
            number_books = even_lines[0]
            #days it takes for library to sign up
            days_signup = even_lines[1]
            #number of books library can ship per day
            shipped_day = even_lines[2]
            #a list of libraries with their values
            """
            [library id, number of books, days to signup, shipped per day possible,
            ids of all of its books]
            """
            library.append(library_id)
            library.append(number_books)
            library.append(days_signup)
            library.append(shipped_day)
            library.append(library_books_ids)
            library_data.append(library)



importdata("d_tough_choices.txt")
