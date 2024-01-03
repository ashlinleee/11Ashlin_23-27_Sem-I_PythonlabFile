def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count
string_test = 'Today is My Best Day'
upper, lower = count_upper_lower(string_test)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
