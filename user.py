class User:
    """
    User class for generating new instances of users.
    """
    users_list = []

    def __init__(self, username, password):
        """
        __init__ method that defines properties of our users objects.
        """
        self.username = username
        self.password = password