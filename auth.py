import questionary
import bcrypt
from models import User
from peewee import *

def ask_password() -> str:
    password = questionary.text("Enter your password: ").ask()
    return password

def ask_username() -> str:
    username = questionary.text("Enter username:").ask()
    return username

def hashing_pass(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def verify_pass(user_password, stored_hash):
    password_bytes = user_password.encode('utf-8')
    stored_hash_bytes = stored_hash.encode('utf-8')
 
    return bcrypt.checkpw(password_bytes, stored_hash_bytes)

def register_user(username: str, password: str) -> User:
    if len(username)==0:
        raise ValueError("Username cannot be empty ")
    if len(password)<6:
        raise ValueError ("Password must contain at least six characters ")

    if User.select().where(User.username == username).exists():
        raise ValueError("Username already exists")
    hashed_password = hashing_pass(password)
    new_user = User.create(username=username, password_hash=hashed_password)
    return new_user

def login_user(username: str, password: str) -> User | None:
    user = User.get_or_none(User.username == username)
    if not user:
        raise ValueError("Not found username")
    if verify_pass(password, user.password_hash):
        return user
    return None

