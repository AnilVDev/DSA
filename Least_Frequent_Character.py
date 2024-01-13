def least_frequent_character(s):
    all_freq = {}
    for i in s:
        if i in all_freq:
            all_freq[i]+=1
        else:
            all_freq[i] = 1
    return min(all_freq,key = all_freq.get)     

test_str = "GeeksforGeeks"
print ("The original string is : " + test_str) 
print(least_frequent_character(test_str))      
