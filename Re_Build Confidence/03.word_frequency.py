phrase = input("Enter a phrase: ").split()
repeated = {}

for word in phrase:
    if word in repeated:
        repeated[word] += 1
    else:
        repeated[word] = 1

print(repeated)