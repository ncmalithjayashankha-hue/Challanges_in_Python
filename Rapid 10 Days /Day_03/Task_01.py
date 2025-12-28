analyze = {"Even":"", "polarity":"","prime":False}
num = int(input("Enter a Number: "))
if num %2 == 0 :
    analyze["even"] = "Even"
else:
    analyze["even"] = "Odd"
if num == 0 :
    analyze["polarity"] = "Zero"
elif num >= 1 :
    analyze["polarity"] = "Positive"
    if num == 2:
        analyze["prime"] = True
elif num < 0 :
    analyze["polarity"] = "Negative"
print(f"""
==== Analyse ====
Number Polarity : {analyze["polarity"]}
Even or Odd     : {analyze["even"]}
Prime           : {analyze["prime"]}
""")