num = 458.541315
rounded_num = num.__round__(2)
x = round(num, 2)
print(rounded_num)
print('%.2f' % num)
print(x)


#numbers = []
#count = 0
#while count < 5:
#    num = float(input('Enter a number: '))
#    numbers.append(num)
#    count +=1
#print(numbers)

with open('test.txt', 'r', encoding='UTF8') as file1:
    content = file1.readlines()
with open('new_file1.txt', 'w') as file1:
    count = 0

    for line in content:
        if count == 4:
            count += 1
            continue
        else:
            file1.write(line)
            count += 1


#names = input(('Enter three names: '))
#name_list = names.split()
#print('Name 1:', name_list[0])
#print('Name 2:', name_list[1])
#print('Name 3:', name_list[2])

totalMoney = 1000
quantity = 3
price = 450
print(f'I have {totalMoney} dollars so I can buy {quantity} footballs for {price} dollars')

quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))

import os

size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')

with open('Test.txt', 'r') as file1:
    content = file1.readlines()
print(content[3])
