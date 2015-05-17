class Cookbook(object):
    def __init__(self, name):
        self.name = name
        self.recipes = []

    @classmethod
    def named(cls, name):
        return Cookbook(name)

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        return self
