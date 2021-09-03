class Credentials:
    """
    Class for  new instances of user credentials
    """
    credentials_list = []

    def __init__(self, account_type, username, password):
        """
        Init method for initializing user credentials objects
        """
        self.account_type = account_type
        self.username = username
        self.password = password

    def save_credentials(self):
        """
        Method to save new instances of credential class.
        """
        Credentials.credentials_list.append(self)