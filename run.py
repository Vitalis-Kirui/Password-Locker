#!/usr/bin/env python3.8
from user import User
from credential import Credentials
import random
import string

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

def find_user_main(username, password):
    """
    Function to find user by username and returns user's credentials.
    """
    return User.find_user(username, password)

def check_existing_users(username, password):
    """
    Function to check users exists using their usernames
    """
    return User.users_exists(username, password)

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

    print("Proceed to Login")
    print('\n')

    print("Enter your username:")
    account_username = input()

    print("Enter your password:")
    account_password = input()
    print('\n')

    if check_existing_users(account_username, account_password):
        """
        Function to check if the user provided in login exists in the users list.
        """
        get_user = find_user_main(account_username, account_password)

        while True:
            print("\n")
            print("Use these abbreviations to perfom operations. : \n\nca - create a new account credential, \nda - display account, \nfa -find an account, \ndl - delete account, \nex -exit the account list ")
            print('\n')

            user_operation = input().lower()

            if user_operation == 'ca':
                print("New Credential Account")
                print("\n")

                print("Enter Account Type")
                account_type = input()

                print("Enter it's Username")
                username = input()
                
                #Password generation
                password_creation = password_choice(
                    "Would you like to have your password generated?(yes/no)"
                )

                if password_creation == "yes":
                    """
                    Autogenerate password code.
                    """
                    value = 16
                    lower = string.ascii_lowercase
                    upper = string.ascii_uppercase
                    num = string.digits
                    all = lower + upper + num
                    temp = random.sample(all, value)
                    password = "".join(temp)

                else:
                    """
                    Password created by user.
                    """
                    print("\n")
                    print("Please Create a password for your account.")
                    password = input()

                #Saving the new credentials
                save_account(create_account(account_type, username, password))
                print('\n')
                print(f"New account: {account_type}  with user name : {username} created :{password}")
                print('\n')

            elif user_operation == 'da':
                if display_account():
                    print("Here is a list of all your accounts")
                    print('\n')

                    for credentials in display_account():
                        print(f"{credentials.account_type} |   {credentials.username} |   {credentials.password}")

                else:
                    print('\n')
                    print("We can't seem to find any accounts saved in your account. \nMake sure have have successfuly created first.")
                    print('\n')

            elif user_operation== 'fa':
                print("Enter the account name you would like to find.")

                find_accounts = input()
                if check_existance(find_accounts):
                    search_account = find_account(find_accounts)
                    print(f"{search_account.account_type}")
                    print("\n")

                    print(f"Account Name ~~~>{search_account.account_type}")
                    print(f"Username ~~~>{search_account.username}")
                else:
                    print("We can find the account you are looking for! \nCheck the account you provided and try again.")
                print('\n')




            else:
                print("I really didn't get that. Please make sure you use the abbreviations to perform an operation.")

    else:
        print("That account does not exist. Please create one")
        print('\n')




if __name__ == '__main__':
    main()
