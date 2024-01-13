def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string

input_string = "i love programming very much"
output_string = reverse_words(input_string)

print(f"Input: {input_string}")
print(f"Output: {output_string}")
