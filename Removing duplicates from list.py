list = [1, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8]
print(list.count(list[0]))
list.remove(1)
list.remove(1)
print(list)


numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
