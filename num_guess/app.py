import random
import time
from pathlib import Path
import hashlib

USER_FILE = "users.txt"
LOG_FILE = "log.txt"
SCORE_FILE = "miniDB.txt"

score = 0
game_running = True

def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

# ---------------- LOGGING ---------------- #

LOGS = {
    1: "Game Started",
    2: "Number Generated",
    3: "Number Entered",
    4: "Number Matched",
    5: "Wrong Guess",
    6: "Score Checked",
    7: "Game Closed",
    8: "Highest Score Updated",
    9: "Authentication Started",
    10: "Authentication Ready",
    11: "Credentials Entered",
    12: "Login Successful",
    13: "Login Failed",
    14: "Too Many Failed Attempts"
}


def write_log(code):
    message = LOGS.get(code, "Unknown Event")
    now = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{now} : {message}\n")


# ---------------- SETUP ---------------- #

def setup():

    print("\nFirst Time Setup\n")

    while True:
        username = input("Create Username : ").strip()
        password = input("Create Password : ").strip()
        confirm = input("Confirm Password : ").strip()

        if password == confirm:
            break

        print("Passwords do not match.\n")

    hashed_user = hash_text(username)
    hashed_pass = hash_text(password)

    with open(USER_FILE, "w") as file:
        file.write(f"{hashed_user},{hashed_pass}")

    with open(SCORE_FILE, "w") as file:
        file.write("0")

    Path(LOG_FILE).touch()

    print("\nSetup Completed Successfully.\n")


# ---------------- AUTH ---------------- #

def authenticate():

    if not Path(USER_FILE).exists():
        setup()

    with open(USER_FILE, "r") as file:
        username, password = file.read().split(",")

    write_log(9)

    attempts = 3

    while attempts:

        print("\nLogin")

        user = input("Username : ").strip()
        pwd = input("Password : ").strip()

        write_log(11)

        if (
                hash_text(user) == username and
                hash_text(pwd) == password
        ):
            write_log(12)
            print("\nLogin Successful\n")
            return True

        attempts -= 1
        write_log(13)

        print(f"Incorrect Username or Password ({attempts} attempts left)")

    write_log(14)
    return False


# ---------------- SCORE ---------------- #

def highest_score():

    try:
        with open(SCORE_FILE, "r") as file:
            return float(file.read())

    except:
        return 0


def save_score(new_score):

    old = highest_score()

    if new_score > old:
        with open(SCORE_FILE, "w") as file:
            file.write(str(new_score))

        write_log(8)
        old = new_score

    print(f"\nHighest Score : {old:.2f}\n")


# ---------------- GAME ---------------- #

def start_game():

    global score

    write_log(1)

    secret = random.randint(1, 100)

    write_log(2)

    attempts = 0

    print("\nGuess the Number (1-100)")
    print("Type E to exit.\n")

    while True:

        guess = input("Your Guess : ").strip()

        if guess.lower() == "e":
            break

        try:
            guess = int(guess)

        except ValueError:
            print("Enter a valid number.")
            continue

        attempts += 1

        write_log(3)

        score = round(10 / attempts, 2)

        if guess == secret:

            print("\nCongratulations!")
            print(f"You guessed it in {attempts} attempts.")
            print(f"Score : {score}")

            write_log(4)

            save_score(score)

            break

        elif guess > secret + 10:
            print("Too High")

        elif guess > secret:
            print("High")

        elif guess < secret - 10:
            print("Too Low")

        else:
            print("Low")

        write_log(5)


# ---------------- MENU ---------------- #

def menu():

    global game_running

    while game_running:

        print("\n===== MENU =====")
        print("1. Start Game")
        print("2. View Highest Score")
        print("3. Exit")

        choice = input("Choice : ").strip()

        if choice == "1":
            start_game()

        elif choice == "2":
            save_score(score)

        elif choice == "3":
            write_log(7)
            game_running = False
            print("\nThank you for playing!")

        else:
            print("Invalid Choice")


# ---------------- MAIN ---------------- #

print("=" * 35)
print("WELCOME TO GUESS THE NUMBER")
print("=" * 35)

if authenticate():
    menu()