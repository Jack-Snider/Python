def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str

    return reversed_str

original_str = "Hello, World!"
reversed_result = reverse_string(original_str)
print(reversed_result)