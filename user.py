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

    def save_user(self):
        """
        This is a save method for saving newly created objects.
        """
        User.users_list.append(self)

    def delete_user(self):
        """
        A delete method for deleting a user from the users list.
        """
        User.users_list.remove(self)

    @classmethod
    def find_user(cls, username):
        """
        Method that takes in the username and return the user account.
        """
        for user in cls.users_list:
            if user.username ==username:
                return user