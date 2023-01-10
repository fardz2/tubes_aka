def permutasi_iteratif(n, r):
    result = 1
    for i in range(r):
        result = result * (n - i)
    return result

print(permutasi_iteratif(5,2))