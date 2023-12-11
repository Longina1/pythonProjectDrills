def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '@'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])

colour_list_1 = set(["White", "Black", "Red"])
colour_list_2 = set(["Red", "Green"])
for x in colour_list_1:
    if x not in colour_list_2:
        print(x)

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1 - color_list_2)
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2 - color_list_1)


