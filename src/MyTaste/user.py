class User(object):
    def __init__(self, name):
        """

        :rtype : User
        """
        self.cookbooks = []
        self.name = name

    @classmethod
    def named(cls, name):
        """
        Name of the user
        :param name: string
        :rtype : User
        """
        return User(name)

    def owns_cookbook(self, cookbook):
        """

        :rtype : User
        """
        self.cookbooks.append(cookbook)
        return self
