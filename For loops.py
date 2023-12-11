for item in 'Python':
    print(item)

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10):
    print(item)

for item in range(5, 10, 2):
    print(item)

prices = [10, 20, 30]
for item in prices:
    print(f'The total value of the shopping cart is  {int(prices[0] + prices[1] + prices[2])}')
    break
print('Next')

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f'Total: {total}')
