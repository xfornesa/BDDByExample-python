from unittest import TestCase
from MyTaste.cookbook import *
from MyTaste.recipe import *


class TestCookbook(TestCase):
    def test_named(self):
        name = 'Desserts'
        cookbook = Cookbook.named(name)
        assert name == cookbook.name

    def test_add_recipe(self):
        cookbook = Cookbook.named('Desserts')
        recipe = Recipe.titled('Crema catalana')

        cookbook.add_recipe(recipe)

        assert cookbook.recipes[0] == recipe
