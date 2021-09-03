import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for out user class.
    """
    def setUp(self):
        """
        Setup method that is run before each test case
        """
        self.new_user = User("Vitalis", "ptalz#75")

    def test__init__(self):
        """
        Test init method to test if objects properties are being initialized properly
        """
        self.assertEqual(self.new_user.username, "Vitalis")
        self.assertEqual(self.new_user.password, "ptalz#75")

    def tearDown(self):
        """
        Method to delete users from users list after every test case
        """
        User.users_list = []

    def test_save_user(self):
        """
        A test method to test if our app is saving the objects/users.
        """
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)

    def test_save_multiple_users(self):
        """
        Method to test if we can save more than one user to our users list.
        """
        self.new_user.save_user()
        testing_user = User("Kipyegon", "PyegonPtalz#75")
        testing_user.save_user()

        self.assertEqual(len(User.users_list), 2)

    def test_delete_user(self):
        """
        Test method to test if the app can delete objects from the list
        """
        self.new_user.save_user()
        testing_user = User("Kipyegon", "PyegonPtalz#75")
        testing_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.users_list), 1)

    def test_find_user(self):
        """
        Method for testing if the app can really find a user by their usernames.
        """
        self.new_user.save_user()
        testing_user = User("Kipyegon", "PyegonPtalz#75")
        testing_user.save_user()

        found_user = User.find_user("Kipyegon")

        self.assertEqual(found_user.password, testing_user.password)

if __name__ == '__main__':
    unittest.main()
