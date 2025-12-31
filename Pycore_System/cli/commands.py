from utils.colors import (
    print_success,
    print_error,
    print_info
)
from utils.spinner import loading
from core.logger import get_logger
from core.database import add_user, list_users
from core.auth import hash_password
from utils.colors import print_warning
from core.auth import authenticate
from core.config import current_user
import core.config as config

logger = get_logger("COMMANDS")

def help_cmd():
    print_info("Available commands:")
    print_info(" help   -> Show this help menu")
    print_info(" status -> System status")
    print_info(" adduser-> Add a new user")
    print_info(" listuser-> List all users")
    print_info(" login  -> Login a user")
    print_info(" logout -> Logout a user")
    print_info(" exit   -> Exit PyCore System")

def status_cmd():
    loading("Checking system status")
    logger.info("Status checked")
    print_success("PyCore System is running normally")

def exit_cmd():
    print_info("Exiting PyCore System....")
    logger.info("PyCore System exited")
    exit(0)

def adduser_cmd():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    hashed = hash_password(password)

    if add_user(username, hashed):
        print_success("User added successfully")
    else:
        print_error("User already exists")

def listuser_cmd():
    users = list_users()

    if not users:
        print_warning("No users found")
        return

    print_info("Users:")
    for uid, uname, role in users:
        print_info(f"{uid} | {uname} | {role}")

def login_cmd():
    if config.current_user:
        print_warning("Already Logging in")
        return
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    user = authenticate(username, password)
    if user:
        config.current_user = user
        print_success(f"Logged in as {user[1]}")
    else:
        print_error("Invalid credentials")

def logout_cmd():
    if not config.current_user:
        print_warning("Not Logging out")
        return
    print_info(f"User {config.current_user[1]} logged out")
    config.current_user = None