use = input("Enter the Numbers to Analyze (Separated By Commas) : ").split(",")
int_list = list(map(int,use))
odd_count = 0
even_count = 0

for x in int_list:
    if x % 2 == 0:
        odd_count += 1
    else:
        even_count += 1


print(f"""
==== List Analyzer ====
Count : {len(int_list)}
sum : {sum(int_list)}
Average : {sum(int_list)/len(int_list)}
Max : {max(int_list)}
Min : {min(int_list)}
Even : {even_count}
Odd : {odd_count}
""")
