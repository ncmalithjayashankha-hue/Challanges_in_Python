phrase = input("Please enter a phrase: ")
vowels = 0

print(f"Characters {len(phrase.split())}")
print(f"Words {len(phrase.split())}")
for ch in phrase.lower():
    if ch in "aeiou":
        vowels += 1
print(f"Vowels {vowels}")