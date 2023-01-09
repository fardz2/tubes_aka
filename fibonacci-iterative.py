def iterative_fibonacci(n):
    # Let f[0] = 0 and f[1] = 1
    f = [0, 1]
    
    # For i = 2 to n
    for i in range(2, n+1):
        # f[i] = f[i-1] + f[i-2]
        f.append(f[i-1] + f[i-2])
    
    # Return f[n]
    return f[n]

print(iterative_fibonacci(2))
