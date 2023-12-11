list1 = [10, 20, 30, 40, 50]
list2 = list1[::-1]

for item in list2:
    print(item)


size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])
