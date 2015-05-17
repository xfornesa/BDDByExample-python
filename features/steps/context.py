from behave import *
from MyTaste.cookbook import *
from MyTaste.recipe import *
from MyTaste.user import *

use_step_matcher("parse")

@given('exists a user named "{user_name:w}" who owns a cookbook named "{cookbook_name:w}"')
def step_impl(context, user_name, cookbook_name):
    """
    :type context behave.runner.Context
    """
    context.user = User.named(user_name)
    context.cookbook = Cookbook.named(cookbook_name)
    context.user.owns_cookbook(context.cookbook)
    pass


@step('exists a recipe of title "{title}"')
def step_impl(context, title):
    """
    :type context behave.runner.Context
    """
    context.recipe = Recipe.titled(title)


@when('the recipe "{recipe_title}" is added to the "{user_name}"\'s cookbook named "{cookbook_name}"')
def step_impl(context, recipe_title, user_name, cookbook_name):
    """
    :type context behave.runner.Context
    """
    user = context.user
    recipe = context.recipe
    cookbook = context.cookbook
    cookbook.add_recipe(recipe)


@then('the "{user_name}"\'s cookbook named "{cookbook_name}" should contain the recipe of title "{recipe_title}"')
def step_impl(context, user_name, cookbook_name, recipe_title):
    """
    :type context behave.runner.Context
    """
    user = context.user
    recipe = context.recipe
    cookbook = context.cookbook

    assert cookbook.recipes[0] == recipe
