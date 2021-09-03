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

def save_user_main(user):
    """
    Function for saving user.
    """
    user.save_user()

def find_user_main(username):
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
    credentials.save_credentials()

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

def delete_account(credentials):
    """
    Function deleting account
    """
    credentials.delete_credentials()
    
def display_account():
    """
    Function that returns all saved account credentials.
    """
    return Credentials.display_credentials()

#End of credential class functions

#Password creation choice

def password_choice(quiz):
    """
    Function that defines mode of password creation.
    """
    user_choice = None
    while user_choice not in ("yes", "no"):
        user_choice = input(quiz).lower()
    return user_choice

#MAIN FUNCTION
def main():
    """
    Main function majorly for user interactions.
    """
    print("Hello there! Welcome to password locker. \nLet us remember and keep your password save for you.")
    print('\n')
    print("First, let's get you set up your account.")
    print('\n')
    print("Please follow the steps to create an account with Password Locker.")
    print('\n')

    print("Create a username")
    username = input()
    print("Create password for you Password Locker account.")
    password = input()

    save_user_main(create_user(username, password))
    print('\n')
    print('\n')

    print(f"Hello {username}, Thank you for creating an account with us.")
    print('\n')

if __name__ == '__main__':
    main()
