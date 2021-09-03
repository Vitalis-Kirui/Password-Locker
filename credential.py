class Credentials:
    """
    Class for  new instances of user credentials
    """
    credentials_list = []

    def __init__(self, account_name, username, password):
        """
        Init method for initializing user credentials objects
        """
        self.account_name = account_name
        self.username = username
        self.password = password