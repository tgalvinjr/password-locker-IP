import unittest
from user import User


class TestUser(unittest.TestCase):
    """Test case for user class behaviour"""

    def setUp(self):
        """Runs Set Up method before each test case to check if the correct instatiation of the class"""
        self.new_user = User("NewUser", "12345")


    def test_init(self):
        """Test to ensure that the object is initialized properly"""
        self.assertEqual(self.new_user.user_name, "NewUser")
        self.assertEqual(self.new_user.password, "12345")

    def test_save_user(self):
        """Method that tests wether a user credentials have been successfully saved"""
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()

