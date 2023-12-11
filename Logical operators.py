has_criminal_record = False
has_good_credit = True
if has_good_credit and not has_criminal_record:
    print('Eligible for loan')

temperature = 30
if temperature > 30:
    print('It is a hot day')
else:
    print('It is not a hot day')

name = input('Enter a name: ')

if len(name) < 3:
    print('The name must be at least 3 characters')
elif len(name) > 50:
    print('The name can be a maximum of 50 characters')
else:
    print('The name looks good')
