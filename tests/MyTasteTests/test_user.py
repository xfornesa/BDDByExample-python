from unittest import TestCase
from MyTaste.user import *
from MyTaste.cookbook import *

class TestUser(TestCase):
    def test_named(self):
        name = 'Xavi'
        user = User.named(name)
        assert name == user.name

    def test_owns_cookbook(self):
        user = User.named('Xavi')
        cookbook = Cookbook.named('Postres')
        user.owns_cookbook(cookbook)

        assert user.cookbooks[0] == cookbook
