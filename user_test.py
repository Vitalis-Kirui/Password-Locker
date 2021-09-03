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

if __name__ == '__main__':
    unittest.main()