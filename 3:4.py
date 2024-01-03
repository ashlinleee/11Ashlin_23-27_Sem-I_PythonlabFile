def per_num(num):
    if num <= 0:
        return False
    sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_of_divisors == num
number = int(input("Enter a number: "))
if per_num(number):
    print(number, "is a perfect number.")
else:
    print(number,"is not a perfect number.")
