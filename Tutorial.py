is_hot = False
is_cold = False


if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print('Wear warm clothes')
else:
    print("It's a lovely day")
print('Enjoy your day')

weight = int(input('Enter your weight: '))
unit = input('Enter L (lbs) if your weight is expressed in ppounds or enter K if your weight is expressed in kilograms: ')
if unit.upper() == "L":
    print('You are :', weight * 0.45, 'kilos')
if unit.upper() == "K":
    print('You are :', weight / 0.45, 'pounds' )
