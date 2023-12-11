import datetime

name = input("What's your name? ")
age = int(input('How old are you? '))
turn_hundred = 100 - age
year = 2023

answer = name, 'you will turn 100 years old in year', int(year + turn_hundred)

n = int(input('Input your number: '))
print(n * answer)
