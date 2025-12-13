try:
    counts = {'a':0,'e':0,'i':0,'o':0,'u':0}
    sentence = input("Enter sentence: ")
    for i in sentence.lower():
        if i in counts:
            counts[i] += 1

    print(f"""
    ==== Vowels Analyze ====
    a : {counts['a']}
    e : {counts['e']}
    i : {counts['i']}
    o : {counts['o']}
    u : {counts['u']}
    """)
except:
    print("Try again")