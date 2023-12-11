a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x < 5:
        print(list([x]))
print([ x for x in a if x<5 ])

n = int(input('Enter a number: '))
for x in a:
    if n > x:
        print(list([x]))
