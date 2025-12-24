text = input("Enter the Text to check: ")
clean_text = text.lower().split()
clean_text_joined = str(''.join(clean_text))
if clean_text_joined == clean_text_joined[::-1]:
    print("Palindrome Text")
else:
    print("Not Palindrome")