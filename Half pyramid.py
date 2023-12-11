for i in range(1,6):
    output = ''
    times = i
    while (times > 0):
        output += '*'
        times = times - 1
    print(output)


for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
