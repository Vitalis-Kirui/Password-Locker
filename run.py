#!/usr/bin/env python3.8
from user import User
from credential import Credentials

#User class functions
def create_user(username, password):
    """
    Function for creating a new user account on our app.
    """
    new_user = User(username, password)
    return new_user

    def save_user(user):
        """
        Function for saving user.
        """
        user.save_user()

    def find_user(username):
        """
        Function to find user by username and returns user's credentials.
        """
        return User.find_user(username)

    def check_existing_users(username):
        """
        Function to check users exists using their usernames
        """
        return User.users_exists(username)

    #End of user class functions

    #Function for Credentials class

    def create_account(account_type, username, password):
        """
        Function that helps users create account.
        """
        new_account = Credentials(account_type, username, password)
        return new_account

    def save_account(credentials):
        """
        Function for saving the new account credentials
        """
        credentials.save_account()

    def find_account(account_type):
        """
        Function for finding using the type of account name.
        """
        return Credentials.find_credentials(account_type)

    def check_existance(account_type):
        """
        Function for checking if an account exists using account tpe name.
        """
        return Credentials.credentials_exists(account_type)