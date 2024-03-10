for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print('*', end=' ')
    print(' ')


#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    return base ** exp

print(exponent(5,4))

