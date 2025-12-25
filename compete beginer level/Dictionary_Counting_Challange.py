phrase_summary = {}
phrase = input("Enter the phrase: ").strip().split()
for word in phrase:
    if word in phrase_summary:
        phrase_summary[word] += 1
    else:
        phrase_summary[word] = 1

print(f"""
{phrase_summary}
""")