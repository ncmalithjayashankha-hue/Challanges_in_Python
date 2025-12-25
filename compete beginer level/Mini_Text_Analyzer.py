def analyzer(text):
    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    count = {}
    for word in text:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
        for char in word:
            if char in vowels:
                vowels[char] += 1
    return vowels

phrase = input("Enter a phrase: ").strip().split()
print(analyzer(phrase))