text = input("Enter the text to Check: ")

caps = 0
for i in text:
    if i.isupper():
        caps += 1
print(caps)