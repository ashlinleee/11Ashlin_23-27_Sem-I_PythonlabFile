def armstrong_no(num):

    num_str = str(num)
    num_digits = len(num_str)

    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num

numo = int(input("Enter a number: "))

if armstrong_no(numo):
    print(f"{numo} is an Armstrong number.")
else:
    print(f"{numo} is not an Armstrong number.")