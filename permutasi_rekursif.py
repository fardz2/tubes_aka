def permutasi_rekursif(n, r):
    if r == 0:
        return 1
    else:
        return permutasi_rekursif(n-1, r) + permutasi_rekursif(n-1, r-1)
hasil = permutasi_rekursif(5, 2)
print(hasil) 