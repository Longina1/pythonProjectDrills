a = [5, 10, 15, 20, 25]
print(a[0], a[-1])

for x in a:
    if x == a[0]:
        print(x)
for x in a:
    if x == a[-1]:
        print(x)

def list_ends(a_list):
    return[a_list[0], a_list[len(a_list)-1]]
print(list_ends([5, 10, 15, 20, 25]))
