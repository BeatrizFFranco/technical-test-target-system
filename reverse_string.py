def reverse_string(s):
    reversed_str = []
    for i in range(len(s) - 1, -1, -1):
        reversed_str.append(s[i])
    return ''.join(reversed_str)

original_string = "Python"
reversed_string = reverse_string(original_string)

print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")