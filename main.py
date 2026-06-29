import bcrypt
import sqlite3 
import pandas as pd

from app_model.db import connection
from app_model.users import add_user, get_user

# hash password using bcrypt
def generate_hash(pwd):
    byte_pwd = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(byte_pwd, salt)
    return hash.decode('utf-8')

# validating the hash vs password 
def is_valid_hash(pwd, hash):
    hash_ =  hash.encode('utf-8')
    byte_pwd = pwd.encode('utf-8')
    is_valid = bcrypt.checkpw(byte_pwd, hash_)
    return is_valid 

# user registration
def user_registration(connection):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    role = input("Enter your role (user/admin): ")
    hashed_password = generate_hash(password)
    add_user(connection, name, hashed_password, role)

    print("User registered successfully!")

# User Login
def user_login(connection):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    id, user_name, user_hash, user_role = get_user(connection, name)
    print(f"Welcome {user_name}!")
    if name == user_name and is_valid_hash(password, user_hash):
        return True
    return False

def main():
    while True:
        print("Welcome to the System!")
        print("Choose an option to continue...")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        if choice == '1':
            user_registration(connection)
        elif choice =='2':
            if user_login(connection):
                print("Login successful!")
            else:
                print("Login failed! Try again.")
        elif choice == '3':
            print("Exiting the system. See you next time!")
            break



if __name__ == '__main__':
    main()



