import random
number = random.randint(0,100)
marks = 100
for i in range (10):
    print()
    guess = int(input("Enter the Number You guess: "))
    if number == guess:
        print(f"WOW User!!! You won this game by {int(i)} attempts")
        break
    elif number>guess:
        print(f"Try a Higher Number than {guess}")
        print(f"You have only {9-i} attempts left")
    else:
        print(f"Try a Lower Number than {guess}")
        print(f"You have only {9-i} attempts left")
print(f"You got {marks/i} marks !!!")