num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add = num1 + num2
print("Addition:",add)

sub = num1 - num2
print("Subtraction:",sub)

mul = num1 * num2
print("Multiplication:",mul)

div = num1 / num2 if num2 != 0 else "Cannot divide by zero"
print("Division:",div)

mod = num1 % num2 if num2 != 0 else "Cannot divide by zero"
print("Modulus:",mod)

greater = num1 > num2
print(num1, ">", num2, ":", greater)

less = num1 < num2
print(num1, "<", num2, ":", less)

greater_equal = num1 >= num2
print(num1, ">=", num2, ":", greater_equal)

less_equal = num1 <= num2
print(num1, "<=", num2, ":", less_equal)

equal_to = num1 == num2
print(num1, "==", num2, ":", equal_to)

not_equal_to = num1 != num2
print(num1, "!=", num2, ":", not_equal_to)