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

    def tearDown(self):
        """
        Method run before every test to clean up the credentials list
        """
        Credentials.credentials_list = []

    def test_save_credentials(self):
        """
        Method to test if save credential function in saving new credentials.
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        """
        A test method to test if our app can save more than one credentials
        """
        self.new_credentials.save_credentials()
        test_credential = Credentials("F-Society", "Free Society", "Fuck#Society")
        test_credential.save_credentials()

        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        """
        A test method to see if our delete credentials function is working.
        """
        self.new_credentials.save_credentials()
        test_credential = Credentials("F-Society", "Free Society", "Fuck#Society")
        test_credential.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credentials(self):
        """
        A test method to check if our find credentials function is working.
        """
        self.new_credentials.save_credentials()
        test_credential = Credentials("F-Society", "Free Society", "Fuck#Society")
        test_credential.save_credentials()

        found_credentials = Credentials.find_credentials("F-Society")

        self.assertEqual(found_credentials.password, test_credential.password)

    def test_credentials_exists(self):
        """
        Test to check what credentials exists function returns when checking if credentials exists in our credentials list.
        """
        self.new_credentials.save_credentials()
        test_credential = Credentials("F-Society", "Free Society", "Fuck#Society")
        test_credential.save_credentials()

        credentials_exists = Credentials.credentials_exists("F-Society")

        self.assertTrue(credentials_exists)

    def test_display_credentials(self):
        """
        A test method on the display credentials function.
        """
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()
