word = input("Enter the word to Check: ")
vowel = 0
for i in word:
    if i in 'aeiouAEIOU':
        vowel += 1

print(vowel)