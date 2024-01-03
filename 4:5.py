class Addition:
    def add_numbers(self, num1, num2):
        return num1 + num2

class UserInput(Addition):
    def get_user_input(self):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = self.add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")


user_input = UserInput()
user_input.get_user_input()

