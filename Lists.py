names = ['John', 'Tom', 'Sarah', 'Emmily', 'Bob', 'Mary']
print(names)
print(names[2])
print(names[-1])
print(names[-2])
print(names[2:])
print(names[2:4])
print(names[:])

numbers = [3, 6, 10, 2, 8, 4]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

