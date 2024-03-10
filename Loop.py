i = 1
while i <= 10:
    print(i)
    i += 1

for i in range(1,6):
    for j in range(i):
        print(i, end=' ')
    print('\n')

print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")

number = int(input('Enter a number: '))
sum = 0
for i in range(1, number + 1):
    sum += i
print(sum)

# s = 0
# n = int(input("Enter number "))
# # run loop n times
# # stop: n+1 (because range never include stop number in result)
# for i in range(1, n + 1, 1):
#     # add current number to sum variable
#     s += i
# print("\n")
# print("Sum is: ", s)

#n = int(input("Enter number "))
# pass range of numbers to sum() function
#x = sum(range(1, n+ 1))
#print('The sume is: ', x)


# number = int(input('Enter a number: '))
# for i in range(1, 11):
#     print(number * i)
# print('')

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for num in numbers:
#     if num > 500:
#         break
#     elif num > 150:
#         continue
#     elif num % 5 == 0:
#         print(num)


# number = str(75869)
# digits = len(number)
# print(digits)



n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()

list1 = [10, 20, 30, 40, 50]
reveresed_list = list1[::-1]
for num in reveresed_list:
    print(num)

for i in range(-10,0):
    print(i)

count = 5
for i in range(count):
        print(i)
else:
    print("Done")


num = int(input('Enter a number: '))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print(factorial)


num = int(input('Enter a number: '))
for i in range(1, num + 1):
    cube = i ** 3
    print('The current number is', i, 'and its cube is', cube)

n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)


for i in range(0,6):
    print('*' * i, end=' ')
    print()


rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
