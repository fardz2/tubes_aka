def permutasi_rekursif(n, r):
    # Basis kasus: jika r = 0, maka hasilnya 1
    if r == 0:
        return 1

    # Rekurens: menghitung P(n, r) dengan menggunakan rumus P(n, r) = P(n-1, r) + P(n-1, r-1)
    else:
        return permutasi_rekursif(n-1, r) + permutasi_rekursif(n-1, r-1)

# Contoh penggunaan fungsi
hasil = permutasi_rekursif(5, 2)
print(hasil)  # Hasilnya: 20