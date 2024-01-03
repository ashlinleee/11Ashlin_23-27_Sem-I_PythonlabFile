start = int(input("Enter start of the range: "))
end = int(input("Enter end of the range: "))
odd_cubes = {num: num ** 3 for num in range(start, end+ 1) if num % 2 != 0}
print("Dictionary of cubes of odd numbers in the range:")
print(odd_cubes)
