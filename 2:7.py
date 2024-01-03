a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# i. Print Complete list
print("Complete List:", a)

# ii. Print 4th element of list
print("4th Element of List:", a[3])

# iii. Print list from 0th to 4th index
print("List from 0th to 4th index:", a[:5])

# iv. Print list -7th to 3rd element
print("List from -7th to 3rd element:", a[-7:4])

# v. Appending an element to list
a.append(110)
print("List after Appending 110:", a)

# vi. Sorting the element of list
a.sort()
print("Sorted List:", a)

# vii. Popping an element
popped = a.pop()
print("Popped Element from List:", popped)
print("List after Popping:", a)

# viii. Removing Specified element
a.remove(40)
print("List after Removing 40:", a)

# ix. Entering an element at specified index
a.insert(2, 35)
print("List after Inserting 35 at index 2:", a)

# x. Counting the occurrence of a specified element
count_50 = a.count(50)
print("Count of 50 in List:", count_50)

# xi. Extending list
a.extend([120, 130])
print("Extended List:", a)

# xii. Reversing the list
a.reverse()
print("Reversed List:", a)
