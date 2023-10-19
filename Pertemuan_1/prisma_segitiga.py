# Menghitung volume prisma segitiga
panjang_alas = float(input("Masukkan Panjang Alas: "))  # Panjang sisi alas segitiga
tinggi = float(input("Masukkan Tinggi: "))  # Tinggi prisma
volume = (panjang_alas * tinggi) / 2
print("Volume prisma segitiga adalah:", volume)

# Menghitung luas permukaan prisma segitiga
luas_permukaan = (2 * panjang_alas) + (3 * tinggi)
print("Luas permukaan prisma segitiga adalah:", luas_permukaan)
