text = 'pynative'
print(text[::2])

def remove_char(text, n):
    x = text[n:]
    return x
print(remove_char('pynative', 4))

for num in range(6):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
