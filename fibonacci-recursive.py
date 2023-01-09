def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
print(recursive_fibonacci(2))