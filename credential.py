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

    def delete_credentials(self):
        """
        Deleting credentials method from our Credentials list.
        """        
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credentials(cls,account_type):
        """
        Class method that finds credentials by taking in user account type and returns credentials related to the account.
        """
        for credentials in cls.credentials_list:
            if credentials.account_type == account_type:
                return credentials

    @classmethod
    def credentials_exists(cls,account_type):
        """
        Class method that checks if credentials exists from our credentials list.
        """
        for credentials in cls.credentials_list:
            if credentials.account_type == account_type:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        Method to return credentials list.
        """
        return cls.credentials_list