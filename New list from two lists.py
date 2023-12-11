list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new_list = []

for n in list1:
    if n % 2 != 0:
        new_list.append(n)

for n in list2:
    if n % 2 == 0:
        new_list.append(n)

print(new_list)
