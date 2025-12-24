phrase = input("Enter the Phrase to continue: ").lower().split()
y = 0
count = {}
for words in phrase:
    if words in count:
        count[words] += 1
    else:
        count[words] = 1
print(f"==== Final Analyze ====")
for word , frequency in count.items():
    print(f"{word} : {frequency}")