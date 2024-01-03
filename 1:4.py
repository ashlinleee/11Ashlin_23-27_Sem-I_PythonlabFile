n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    sum = 0
    print("First",n,"natural numbers:")
    for i in range(1, n + 1):
        print(i)
        sum+= i
    print("Sum of first",n, "natural numbers:",sum)
