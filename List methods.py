numbers = [5, 2, 1, 7, 4]
numbers.append(10)
print(numbers)

numbers.insert(0, 20)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(2))

print(50 in numbers)

print(numbers.count(4))

print(numbers.sort())

numbers.sort()
print(numbers)

numbers.sort()
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(100)
print(numbers2)
