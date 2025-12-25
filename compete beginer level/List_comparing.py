list_01 = [1,2,3,4,5,6,7,8,9,0]
list_02 = [11,22,3,4,55,67,76]
list_03 = []
for item in list_01:
    if item in list_02:
        list_03.append(item)
print(list_03)