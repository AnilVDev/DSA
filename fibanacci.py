def fibanacci(n):
    if n <= 1:
        return n
    else:
        return fibanacci(n-1) + fibanacci(n-2)
    
num = 10
for i in range(num):
    print(fibanacci(i), end=' ')
