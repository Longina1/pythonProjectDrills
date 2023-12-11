customer = {
    'name': 'John Smith',
    'age': 30,
    'is _verified': True

}
print(customer['name'])
print(customer.get('birthdate', '1 Jan 1980'))
customer['name'] = 'Jack Smith'
print(customer['name'])
customer['birthdate'] = '1 MArch 1991'
print(customer['birthdate'])
