number = int(input('Enter a number: '))

sum = 0
for i in range(1, number + 1, 1):
    sum += i
print(sum)

# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)
