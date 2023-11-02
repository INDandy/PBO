import tkinter as tk
from math import pi

def hitung_luas_dan_volume():
    sisi = float(entry_sisi.get())
    bentuk_bangun = combo_bangun.get()
    
    if bentuk_bangun == "Kubus":
        luas = 6 * (sisi ** 2)
        volume = sisi ** 3
    elif bentuk_bangun == "Prisma Segitiga":
        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())
        luas = 2 * (alas * tinggi + 0.5 * sisi * tinggi) + 3 * (sisi ** 2)
        volume = sisi * alas * tinggi
    elif bentuk_bangun == "Balok":
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())
        luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        volume = panjang * lebar * tinggi
    # Tambahkan kasus lainnya sesuai dengan bangun ruang yang Anda inginkan
    else:
        luas = volume = 0

    # Menampilkan hasil dalam widget Entry yang digunakan sebagai latar belakang
    entry_hasil.delete(0, tk.END)  # Hapus teks sebelumnya
    entry_hasil.insert(0, f"Luas {bentuk_bangun}: {luas} satuan luas\nVolume {bentuk_bangun}: {volume} satuan volume")
    entry_hasil.config(state="readonly")


# Membuat jendela aplikasi
app = tk.Tk()
app.title("Kalkulator Bangun Ruang")

# Label dan input untuk panjang sisi (umum)
label_sisi = tk.Label(app, text="Panjang Sisi:")
label_sisi.pack()

entry_sisi = tk.Entry(app)
entry_sisi.pack()

# Dropdown untuk memilih bentuk bangun ruang
label_bangun = tk.Label(app, text="Pilih Bentuk Bangun Ruang:")
label_bangun.pack()

bangun_ruang_options = ["Kubus", "Prisma Segitiga", "Balok", "Limas Segiempat", "Tabung", "Kerucut", "Bola"]
combo_bangun = tk.StringVar(app)
combo_bangun.set(bangun_ruang_options[0])  # Default pilihan
dropdown_bangun = tk.OptionMenu(app, combo_bangun, *bangun_ruang_options)
dropdown_bangun.pack()

# Label dan input tambahan untuk bentuk bangun ruang tertentu (Prisma Segitiga, Balok, dll.)
label_alas = tk.Label(app, text="Alas (Hanya untuk Prisma Segitiga):")
entry_alas = tk.Entry(app)

label_panjang = tk.Label(app, text="Panjang (Hanya untuk Balok):")
entry_panjang = tk.Entry(app)

label_lebar = tk.Label(app, text="Lebar (Hanya untuk Balok):")
entry_lebar = tk.Entry(app)

label_tinggi = tk.Label(app, text="Tinggi:")
entry_tinggi = tk.Entry(app)

# Memasukkan input tambahan ke dalam jendela
label_alas.pack()
entry_alas.pack()

label_panjang.pack()
entry_panjang.pack()

label_lebar.pack()
entry_lebar.pack()

label_tinggi.pack()
entry_tinggi.pack()

# Tombol untuk menghitung luas dan volume
button_hitung = tk.Button(app, text="Hitung Luas & Volume", command=hitung_luas_dan_volume)
button_hitung.pack()

# Entry yang digunakan sebagai latar belakang untuk menampilkan hasil
entry_hasil = tk.Entry()
entry_hasil.pack()

# Menjalankan aplikasi
app.mainloop()
