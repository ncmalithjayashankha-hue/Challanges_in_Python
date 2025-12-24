try:
    text = input("Please enter a text: ")
    analyze = {"upper":0,"lower":0,"digits":0,"special":0,"Spaces":0}
    for ch in text:
        if ch.isupper():
            analyze["upper"] += 1
        elif ch.islower():
            analyze["lower"] += 1
        elif ch.isdigit():
            analyze["digits"] += 1
        elif ch == " ":
            analyze["Spaces"] += 1
        else:
            analyze["special"] += 1
    print(f"""
    ====Final Results====
    Uppercase Letters:{analyze["upper"]}
    Lowercase Letters:{analyze["lower"]}
    Digits:{analyze["digits"]}
    Special Characters:{analyze["special"]}
    """)
except ValueError:
    print("Please Try Again")