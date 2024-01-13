def replace_alphabet(s, n):
    result=''
    for char in s:
        if char.isalpha():
          is_upper = char.isupper()
          new_position =  (ord(char.lower()) - ord('a') + n) % 26
          if is_upper:
             new_char = chr(new_position + ord('A'))
          else:
             new_char = chr(new_position + ord('a'))
          result += new_char
        else:
           result += char
    return result            
                


input_string = "Hello, World!"
shift_value = 3
output_string = replace_alphabet(input_string, shift_value)

print(f"Input: {input_string}")
print(f"Output: {output_string}")
