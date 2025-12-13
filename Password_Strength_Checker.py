pwd = input("Enter the Password to Check: ")
specials = "!@#$%^&*()_-+=,./;'[]<>?:"

is_lower = any(ch.islower() for ch in pwd)
is_upper = any(ch.isupper() for ch in pwd)
has_digit = any(ch.isdigit() for ch in pwd)
has_special = any(ch in specials for ch in pwd)


if len(pwd) < 6:
    print("Weak Password")
elif (len(pwd) >= 8) and is_lower and is_upper and has_digit and has_special:
    print("Strong Password")
else:
    print("Medium Password")