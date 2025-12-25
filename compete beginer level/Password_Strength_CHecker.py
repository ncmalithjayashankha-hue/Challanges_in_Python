def check_strength(pwd):
    spc_chr = "!@#$%^&*()-_=+"
    spc_state = False
    for ch in pwd:
        if ch in spc_chr:
            spc_state = True
    if len(pwd) < 8:
        print("Password is too short")
    elif pwd.islower():
        print("Password must contain with Uppercase letters too")
    elif pwd.isupper():
        print("Password must contain with lowercase letters too")
    elif pwd.isdigit():
        print("Password must contain with characters too")
    elif pwd.isalpha():
        print("Password must contain with numbers too")
    elif not spc_state:
        print("Password must contain with Special Characters too")
    else:
        print("Strong Password")
inpt_pwd = input("Enter Password: ")
check_strength(inpt_pwd)