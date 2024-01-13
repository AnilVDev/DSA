def remove_ith(s,i):
    if i == 0:
        return s[1:]
    return s[0] + remove_ith(s[1:],i-1)

test_str = "GeeksForGeeks"
new_str = remove_ith(test_str, 12)
print("The string after removal of ith character:", new_str)