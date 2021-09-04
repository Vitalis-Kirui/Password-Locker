#!/usr/bin/env python3.8
from user import User
from credential import Credentials
import random
import string

# User class functions


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

# End of user class functions

# Function for Credentials class


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

# End of credential class functions

# Password creation choice


def password_choice(quiz):
    """
    Function that defines mode of password creation.
    """
    user_choice = None
    while user_choice not in ("yes", "no"):
        user_choice = input(quiz).lower()
    return user_choice

# MAIN FUNCTION


def main():
    """
    Main function majorly for user interactions.
    """
    print('\n')
    print("Hello there! Welcome to password locker. \nLet us remember and keep your password save for you.")
    print('\n')
    print("First, let's get you set up your account.")
    print('\n')
    print("Please follow the steps to create an account with Password Locker.")
    print('\n')

    print("Create a username")
    print('~' * 17)
    username = input()
    print('\n')
    print("Create password for you Password Locker account.")
    print('~' * 47)
    password = input()
    print('\n')

    save_user_main(create_user(username, password))
    print('_'*70)
    print("\n")

    print(f"Hello {username}, Thank you for creating an account with us.")
    print('\n')

    print("Proceed to Login")
    print('\n')

    print("Enter your username:")
    print('~' * 20)
    account_username = input()
    print('\n')

    print("Enter your password:")
    print('~' * 20)
    account_password = input()
    print('\n')

    if check_existing_users(account_username, account_password):
        """
        Function to check if the user provided in login exists in the users list.
        """
        get_user = find_user_main(account_username, account_password)

        while True:
            print("\n")
            print("Use these abbreviations to perfom operations.")
            print("~"*44)
            print("1. ca ~~~>To create and save new account credentials.")
            print("2. da ~~~>To display your saved accounts credentials.")
            print("3. fa ~~~>To find a saved account credentials.")
            print("4. dl ~~~>To delete an existing account credentials.")
            print("5. ex ~~~>To log out/exit your Password Locker account.")
            print('\n')
            print("What would you like to do?")
            print("~"*26)
            user_operation = input().lower()
            print("\n")

            if user_operation == 'ca':
                print("New Credential Account")
                print("~"*22)

                print("Enter Account Type")
                print("~"*18)
                account_type = input()
                print("\n")

                print("Enter it's Username")
                print("~"*19)
                username = input()
                print("\n")

                # Password generation
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
                    print("~"*41)
                    password = input()

                # Saving the new credentials
                save_account(create_account(account_type, username, password))
                print('\n')
                print("ACCOUNT CREDENTIALS SUCCESSFULLY SAVED.")
                print("~"*38)
                print(f"TYPE~~~>{account_type} account.")
                print(f"USERNAME~~~>{username}")
                print(f"PASSWORD~~~>{password}")
                print('\n')

            elif user_operation == 'da':
                if display_account():
                    print("Here is a list of all your accounts")
                    print('~'*35)

                    for credentials in display_account():
                        print(f"TYPE~~~>{credentials.account_type} account.")
                        print(f"USERNAME~~~>{credentials.username}")
                        print(f"PASSWORD~~~>{credentials.password}")
                        print('-'*33)

                else:
                    print('\n')
                    print(
                        "We can't seem to find any accounts saved in your account. \nMake sure have have successfuly created first.")
                    print('\n')

            elif user_operation == 'fa':
                print("Enter the account name you would like to find.")
                print('~'*45)
                find_accounts = input()
                print('\n')

                if check_existance(find_accounts):
                    search_account = find_account(find_accounts)
                    print("RESULTS")
                    print("~"*7)
                    print(f"Account Name ~~~>{search_account.account_type}")
                    print(f"Username ~~~>{search_account.username}")
                    print(f"Password ~~~>{search_account.password}")
                else:
                    print(
                        "We can find the account you are looking for! \nCheck the account you provided and try again.")
                print('\n')

            elif user_operation == 'dl':
                print("Enter name of account to delete")
                print("~"*31)
                find_accounts = input()
                print("\n")

                if check_existance(find_accounts):
                    search_account = find_account(find_accounts)
                    delete_account(search_account)
                    print(
                        f"{search_account.account_type}Account deleted successfully")
                else:
                    print('\n')
                    print(
                        "We can find the account you are looking for! \nCheck the accounts you have and try again.")

            elif user_operation == "ex":
                print("Thanks for choosing Password Locker. Bye.")
                break

            else:
                print(
                    "I  didn't get that. Please make sure you use the abbreviations to perform an operation.")

    else:
        print("That account does not exist. Please create one")
        print('\n')


if __name__ == '__main__':
    main()
