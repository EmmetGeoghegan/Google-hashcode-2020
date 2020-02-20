def importdata(filename):
    with open(f"./inputdata/{filename}", "r") as inputfile:
        lines = inputfile.readlines()
        #even readlines
        count = 0
        library_data = []
        for i in range(2, 6, 2):
            library = []
            count += 1
            library_id = count
            #book_ids are on all the odd lines
            book_ids =  lines[i+1].strip("\n").split(" ")
            #splits even lines into the three values to be extracted
            even_lines = lines[i].strip("\n").split(" ")
            number_books = even_lines[0]
            days_signup = even_lines[1]
            shipped_day = even_lines[2]
            #a list of libraries with their values
            library.append(library_id, number_books, days_signup,
                                shipped_day, book_ids)
            library_data.append(library)
    print(library_data)


importdata("a_example.txt")
