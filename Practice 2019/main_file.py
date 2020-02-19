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


def scoring_function(album):
    # get length of album
    leader = 1
    follower = 0
    album_score = []
    while leader < len(album):
        page1 = album[follower]
        page2 = album[leader]

        # check intersection
        inter_score = len(page1.tags.intersection(page2.tags))

        # check page1 comp
        page1_comp = len(page1.tags.difference(page2.tags))

        # check page2 comp
        page2_comp = len(page2.tags.difference(page2.tags))
        album_score.append(min([inter_score, page1_comp, page2_comp]))

    score = sum(album_score)
    return score


importdata("a_example.txt")
for i in c.Image.all_images:
    print(i)
