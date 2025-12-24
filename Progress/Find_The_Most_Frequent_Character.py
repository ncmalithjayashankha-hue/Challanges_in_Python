
text = input("Enter the text: ").lower().replace(" ","")
count = {}
for ch in text:
    if ch not in count:
        count.update({ch:1})
    else:
        count[ch] += 1
for keys,values in count.items():
    print(f"{keys} : {values}")
max_num = max(count, key=count.get)
print(f"letter {max_num} has the most frequent characters, Its {count[max_num]} times")