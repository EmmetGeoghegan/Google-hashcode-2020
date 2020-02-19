class Image:
    all_images = []

    def __init__(self, type, numTags, tags, id):
        self.type = type
        self.numTags = numTags
        self.tags = tags
        self.id = id
        Image.all_images.append(self)

    def __repr__(self):
        return(f"{self.id}, {self.type}, {self.numTags}, {self.tags}")

class Album:
    all_slides = []
    def __init__(self, images):
        self.images = images
        Album.all_slides.append(self)

    def getNumPics(self):
        len(self.images)

    def getTags(self):
        tags = {}

        for image in self.images:
            tags.add(image.tags)
