str = 'pynative'
print(str[0], str[2], str[4], str[6])

word = input('Enter a phrase: ')
print('Original string: ', word)
size = len(word)
print('Printing only even index char')
for i in range(0, size + 1, 2):
    print('index [', i, ']', word[i])


word = input('Enter a phrase: ')
print('Original string: ', word)
x = list(word)
for i in x[0::2]:
    print(i)
