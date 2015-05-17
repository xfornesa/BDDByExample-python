from MyTaste.in_memory_cookbook_repository import *
from MyTaste.in_memory_recipe_repository import *
from MyTaste.in_memory_user_repository import *


def before_scenario(context, scenario):
    """
    :type context behave.runner.Context
    :type context: behave.model.Scenario
    """
    context.cookbooks = InMemoryCookbookRepository()
    context.recipes = InMemoryRecipeRepository()
    context.users = InMemoryUserRepository()
