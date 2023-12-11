def in_group_of_values(value):
    group = [1, 5, 8, 3]
    return value in group
print(in_group_of_values(8))

def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))


