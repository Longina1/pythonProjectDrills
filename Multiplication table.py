n = 2
for i in range(1, 11):
    print(n * i)

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if (i > 500): break
    elif (i > 150): continue
    elif i % 5 == 0:
        print(i)

number = 75869
number_as_str = str(number)
print(len(number_as_str))








