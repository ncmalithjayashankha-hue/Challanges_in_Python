import random
number = int(random.randint(0, 100))
guess = 0
while not number == guess:
    guess = int(input("Enter the Number you Guess: "))
    if guess > number:
        print(f"Try a Lower number than {guess}")
    else:
        print(f"Try a Higher number than {guess}")
print()
print()
print(f"""You won the game successfully
actual number is {number} and you guessed {guess}
""")
