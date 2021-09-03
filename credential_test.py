import unittest
from credential import Credentials

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for credentials class.
    """

    def setUp(self):
        """
        Setup method which is run first everytime we run a test.
        """
        self.new_credentials = Credentials("Twitter", "Cheborgei", "Cheborgei#Sambu")

    def test_init_(self):
        """
        Test init method to test if objects properties are being initialized properly
        """
        self.assertEqual(self.new_credentials.account_type, "Twitter")
        self.assertEqual(self.new_credentials.username, "Cheborgei")
        self.assertEqual(self.new_credentials.password, "Cheborgei#Sambu")

    def test_save_credentials(self):
        """
        Method to test if save credential function in saving new credentials.
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

if __name__ == '__main__':
    unittest.main()