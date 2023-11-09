from math import pi, sqrt
def hitung_luas(jenis_bangun, panjang, lebar, tinggi, jari_kerucut,sisi,alas,tinggi_limas,alas_limas,luas,jari_tabung,tinggi_tabung,tinggi_kerucut,pi,jari_bola):
    if jenis_bangun == "Kubus":
        luas = 6 * (sisi ** 2)
        return luas
    elif jenis_bangun == "Prisma Segitiga":
        luas = 2 * (alas * tinggi + 0.5 * sisi * tinggi) + 3 * (sisi ** 2)
        return luas
    elif jenis_bangun == "Balok":
        luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        return luas
    elif jenis_bangun == "Limas Segiempat":
        luas = alas_limas + 4 * (0.5 * sisi * tinggi_limas)
        return luas
    elif jenis_bangun == "Limas Segitiga":
        luas = 0.5 * alas_limas * tinggi_limas
        return luas
    elif jenis_bangun == "Tabung":
        luas = 2 * pi * jari_tabung * (jari_tabung + tinggi_tabung)
        return luas
    elif jenis_bangun == "Kerucut":
        luas = pi * jari_kerucut * (jari_kerucut + sqrt(jari_kerucut**2 + tinggi_kerucut**2))
        return luas
    elif jenis_bangun == "Bola":
        luas = 4 * pi * (jari_bola ** 2)
        return luas

def hitung_volume(jenis_bangun, panjang, lebar, tinggi, jari_kerucut,sisi,alas,tinggi_limas,alas_limas,luas,jari_tabung,tinggi_tabung,tinggi_kerucut,pi,jari_bola):
    if jenis_bangun == "Kubus":
        volume = sisi ** 3
        return volume
    elif jenis_bangun == "Prisma Segitiga":
        volume = sisi * alas * tinggi
        return volume
    elif jenis_bangun == "Balok":
        volume = panjang * lebar * tinggi
        return volume
    elif jenis_bangun == "Limas Segiempat":
        volume = (0.5 * sisi * tinggi_limas * alas_limas) / 3
        return volume
    elif jenis_bangun == "Limas Segitiga":
        volume = (1/3) * luas * tinggi_limas
        return volume
    elif jenis_bangun == "Tabung":
        volume = pi * (jari_tabung ** 2) * tinggi_tabung
        return volume
    elif jenis_bangun == "Kerucut":
        volume = (pi * (jari_kerucut ** 2) * tinggi_kerucut) / 3
        return volume
    elif jenis_bangun == "Bola":
        volume = (4/3) * pi * (jari_bola ** 3)
        return volume