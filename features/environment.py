def before_scenario(context, scenario):
    """
    :type context behave.runner.Context
    :type context: behave.model.Scenario
    """
    context.users = []
    context.cookbooks = []
    context.recipes = []

