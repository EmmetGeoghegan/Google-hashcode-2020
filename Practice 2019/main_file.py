import time
from classes import classes as c


def importdata(filename):
    with open(f"./input/{filename}") as inputfile:
        lines = inputfile.readlines()
        for id, i in enumerate(lines[1:]):
            i = i.split(" ")
            photo_type = i[0]
            photo_tag_count = i[1]
            tags = [x.strip("\n") for x in i[2:]]
            c.Image(photo_type, photo_tag_count, tags, id)


def createoutputfile(Album, filename="sub.txt"):
    timestamp = str(time.time()).replace(".", "")
    with open(f"./submissions/{timestamp}{filename}", "w+") as outputfile:
        outputfile.write(len(Album.all_slides)+"\n")
        for i in Album.all_slides:
            outputfile.write(" ".join([str(x.id) for x in i.images])+"\n")


def divide_list(my_list, n=2):
    output = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]
    return output


# Create all our image objects
importdata("a_example.txt")

# Create a slide from every horizontal image
for i in c.Image.all_horizontals:
    c.Slide([i])


test = divide_list(c.Image.all_verticals)

for i in test:
    c.Slide(i)

test_album = c.Album(c.Slide.all_slides)
print(test_album.score)
print(test_album)
