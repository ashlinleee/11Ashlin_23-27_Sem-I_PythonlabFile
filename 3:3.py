def get_unique_elements(input_list):
    return list(set(input_list))
# Example list
og_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_elements = get_unique_elements(og_list)
print("Original List:", og_list)
print("List with Distinct Elements:", unique_elements)
