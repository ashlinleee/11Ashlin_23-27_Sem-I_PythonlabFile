rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
    
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()
    
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()


