num_list = input("Enter the Numbers (Separated by commas): ").strip().split(",")
int_num_list = list(map(int, num_list))
state = {"Positive":0,"Negative":0,"Zero":0}

for num in int_num_list:
    if num < 0:
        state["Negative"] += 1
    elif num > 0:
        state["Positive"] += 1
    else:
        state["Zero"] += 1
print(f"""
==== Report ====
Positive : {state["Positive"]}
Negative : {state["Negative"]}
Zero     : {state["Zero"]}
""")