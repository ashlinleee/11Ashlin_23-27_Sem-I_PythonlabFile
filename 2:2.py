my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print("Traversing list in reverse using reverse() method:")
for item in my_list:
    print(item)
    
    
my_list = [1, 2, 3, 4, 5]
print("Traversing list in reverse using slicing:")
for item in my_list[::-1]:
    print(item)
