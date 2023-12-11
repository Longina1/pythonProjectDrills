for x in range(4):
    print(x)

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print('x' * numbers[0])
    print('x' * numbers[1])
    print('x' * numbers[2])
    print('x' * numbers[3])
    print('x' * numbers[4])
    break

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)



numbers = [1, 1, 1, 1, 5  ]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
