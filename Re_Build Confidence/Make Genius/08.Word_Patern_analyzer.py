words_dict = {}
lines_common = {0:""}
while True:
    lines_common[0] += 1
    texts = input("Enter the text('END' to quit): ").strip().split()
    if not texts:
        continue
    if texts[0].upper() == "END" and len(texts) == 1:
        print("Good Bye User...!!!!")
        break
    for words in texts:
        if words not in words_dict:
            words_dict[words.lower()] = 1
        else:
            words_dict[words.lower()] += 1
    most_common = max(lines_common, key=lines_common.get)
    print("Common word in line")

print(f"""
==== Word Pattern Analyze Report ====
line 1 Common Word{most_common}
""")