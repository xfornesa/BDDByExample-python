from unittest import TestCase
from MyTaste.recipe import *

class TestRecipe(TestCase):
    def test_named(self):
        title = 'Crema catalana'
        recipe = Recipe.titled(title)
        assert title == recipe.title

