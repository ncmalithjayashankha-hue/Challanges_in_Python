challenge = input("Enter the Challenge: ").title().split()

clean = []
for word in challenge:
    new_word = ""
    for ch in word:
        if ch.isalnum():      # keep only letters & numbers
            new_word += ch
    if new_word:              # only add if not empty
        clean.append(new_word)
print()
print("_".join(clean))
