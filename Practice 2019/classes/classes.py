
global globalId
class Image:

    def __init__(self, type, numTags, tags):
        self.type = type
        self.numTags = numTags
        self.tags = tags

        self.id = globalId + 1

class Slide:

    def __init__(self, images):
        self.images = images

    def getNumPics(self):
        len(self.images)

    def getTags(self):
        tags = {}

        for image in self.images:
            tags.add(image.tags)
