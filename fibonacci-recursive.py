def recursive_fibonacci(n):
    # If n = 0 or n = 1, return n
    if n == 0 or n == 1:
        return n
    # Otherwise, return RECURSIVE-FIBONACCI(n-1) + RECURSIVE-FIBONACCI(n-2)
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

print(recursive_fibonacci(2))