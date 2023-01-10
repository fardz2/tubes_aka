def permutationIterative(n, r):
    result = 1
    for i in range(r):
        result = result * (n - i)
    return result

print(permutationIterative(5,2))