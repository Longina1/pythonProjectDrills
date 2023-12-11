word = list(input('Enter a word: '))
if word[0] == word[-1] and word[1] == word[-2] and word[2] == word[-3]:
    print('Your word is a palindrome')
