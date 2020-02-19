class Image:
    all_images = []
    all_verticals = []
    all_horizontals = []

    def __init__(self, type, numTags, tags, id):
        self.type = type
        self.numTags = numTags
        self.tags = tags
        self.id = id
        Image.all_images.append(self)
        if self.type == "H":
            Image.all_horizontals.append(self)
        else:
            Image.all_verticals.append(self)

    def __repr__(self):
        return f"{self.id}"
        # return(f"{self.id}, {self.type}, {self.numTags}, {self.tags}")


class Slide:
    all_slides = []
    all_vertical_slides = []
    all_horizontal_slides = []

    def __init__(self, images):
        self.images = images
        self.tags = self.get_tags()
        Slide.all_slides.append(self)
        self.sort_type()

    def get_tags(self):
        all_tags = set()
        for i in self.images:
            for j in i.tags:
                all_tags.add(j)
        return all_tags

    def sort_type(self):
        for i in self.images:
            if i.type == "H":
                Slide.all_horizontal_slides.append(self)
            else:
                Slide.all_vertical_slides.append(self)

    def __repr__(self):
        return f"images on this slide: {[i.id for i in self.images]}"


class Album:
    all_albums = []

    def __init__(self, slides):
        self.slides = slides
        Album.all_albums.append(self)
        self.score = self.scoring_function()

    def scoring_function(self):
        # get length of album
        leader = 1
        follower = 0
        album_score = []
        while leader < len(self.slides):
            page1 = self.slides[follower]
            page2 = self.slides[leader]
            print(page1.tags)
            print(page2.tags)

            # check intersection
            inter_score = len(page1.tags.intersection(page2.tags))
            print(f"inter: {inter_score}")
            # check page1 comp
            page1_comp = len(page1.tags.difference(page2.tags))
            print(f"page1_comp: {page1_comp}")

            # check page2 comp
            page2_comp = len(page2.tags.difference(page2.tags))
            print(f"page2_comp: {page2_comp}")

            album_score.append(min([inter_score, page1_comp, page2_comp]))

            leader += 1
            follower += 1
        score = sum(album_score)
        return score

    def __repr__(self):
        return str([i.images for i in self.slides])
