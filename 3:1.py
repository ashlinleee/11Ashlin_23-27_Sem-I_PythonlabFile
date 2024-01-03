og_list = [1, 2, 3]
print("Original List:", og_list)

# i. Using + operator to extend a list
extended_with_plus = og_list + [4, 5]
print("Extended with + operator:", extended_with_plus)

# ii. Using append() method to add a single element to the list
og_list.append(4)
og_list.append(5)
print("Extended with append():", og_list)

# iii. Using extend() method to add multiple elements to the list
og_list = [1, 2, 3]  
og_list.extend([4, 5])
print("Extended with extend():", og_list)
