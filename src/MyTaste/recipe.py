class Recipe(object):
    def __init__(self, title):
        self.title = title

    @classmethod
    def titled(cls, title):
        return Recipe(title)

