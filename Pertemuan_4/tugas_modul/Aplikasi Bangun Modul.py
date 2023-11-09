import tkinter as tk
from tkinter import ttk
from rumus import hitung_luas, hitung_volume
from math import pi, sqrt
def hitung_luas_dan_volume():
    bentuk_bangun = combo_bangun.get()
    alas = float(entry_alas.get()) if entry_alas.get() else 0.0
    panjang = float(entry_panjang.get()) if entry_panjang.get() else 0.0
    lebar = float(entry_lebar.get()) if entry_lebar.get() else 0.0
    tinggi = float(entry_tinggi.get()) if entry_tinggi.get() else 0.0
    sisi = float(entry_sisi.get()) if entry_sisi.get() else 0.0
    alas_limas = float(entry_alas_limas.get()) if entry_alas_limas.get() else 0.0
    tinggi_limas = float(entry_tinggi_limas.get()) if entry_tinggi_limas.get() else 0.0
    jari_tabung = float(entry_jari_tabung.get()) if entry_jari_tabung.get() else 0.0
    tinggi_tabung = float(entry_tinggi_tabung.get()) if entry_tinggi_tabung.get() else 0.0
    jari_kerucut = float(entry_jari_kerucut.get()) if entry_jari_kerucut.get() else 0.0
    tinggi_kerucut = float(entry_tinggi_kerucut.get()) if entry_tinggi_kerucut.get() else 0.0
    jari_bola = float(entry_jari_bola.get()) if entry_jari_bola.get() else 0.0


    luas = 0.0
    volume = 0.0

    luas = hitung_luas(bentuk_bangun, panjang, lebar, tinggi, jari_kerucut,sisi,alas,tinggi_limas,alas_limas,luas,jari_tabung,tinggi_tabung,tinggi_kerucut,pi,jari_bola)
    volume = hitung_volume(bentuk_bangun, panjang, lebar, tinggi, jari_kerucut,sisi,alas,tinggi_limas,alas_limas,luas,jari_tabung,tinggi_tabung,tinggi_kerucut,pi,jari_bola)
    hasil_luas_entry = f"Luas {bentuk_bangun}: {luas}"
    hasil_volume_entry = f"Volume {bentuk_bangun}: {volume}"

    entry_hasil_luas.insert(tk.END, hasil_luas_entry)
    entry_hasil_luas.config(state="readonly")

    entry_hasil_volume.insert(tk.END, hasil_volume_entry)
    entry_hasil_volume.config(state="readonly")




# Membuat jendela aplikasi
app = tk.Tk()
app.title("Kalkulator Bangun Ruang")


label_bangun = tk.Label(app, text="Pilih Bentuk Bangun Ruang:")
label_bangun.pack()
bangun_ruang_options = ["Kubus", "Prisma Segitiga", "Balok", "Limas Segiempat","Limas Segitiga", "Tabung", "Kerucut", "Bola"]
combo_bangun = tk.StringVar(app)
combo_bangun.set(bangun_ruang_options[0])  # Default pilihan
dropdown_bangun = tk.OptionMenu(app, combo_bangun, *bangun_ruang_options)
dropdown_bangun.pack()


label_sisi = tk.Label(app, text="Sisi: (Kubus,P.Segitiga,Balok,L.Segitiga/Segiempat,)")
label_sisi.pack()

entry_sisi = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)
entry_sisi.pack()

label_alas = tk.Label(app, text="Alas (Prisma Segitiga):")
entry_alas = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_panjang = tk.Label(app, text="Panjang (Balok, Prisma Segitiga):")
entry_panjang = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_lebar = tk.Label(app, text="Lebar (Balok,Prisma Segitiga):")
entry_lebar = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_tinggi = tk.Label(app, text="Tinggi: ")
entry_tinggi = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_alas_limas = tk.Label(app, text="Alas Limas (Limas Segiempat/Segitiga):")
entry_alas_limas = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_tinggi_limas = tk.Label(app, text="Tinggi Limas (Limas Segiempat/Segitiga):")
entry_tinggi_limas = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_jari_tabung = tk.Label(app, text="Jari-jari Tabung (Tabung):")
entry_jari_tabung = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_tinggi_tabung = tk.Label(app, text="Tinggi Tabung (Tabung):")
entry_tinggi_tabung = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_jari_kerucut = tk.Label(app, text="Jari-jari Kerucut (Kerucut):")
entry_jari_kerucut = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_tinggi_kerucut = tk.Label(app,text="Tinggi Kerucut (Kerucut):")
entry_tinggi_kerucut = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

label_jari_bola = tk.Label(app, text="Jari-jari Bola (Bola):")
entry_jari_bola = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30,)

# Menentukan posisi widget entry
label_tinggi.pack()
entry_tinggi.pack()

label_panjang.pack()
entry_panjang.pack()

label_alas.pack()
entry_alas.pack()



label_lebar.pack()
entry_lebar.pack()

label_alas_limas.pack()
entry_alas_limas.pack()

label_tinggi_limas.pack()
entry_tinggi_limas.pack()

label_jari_tabung.pack()
entry_jari_tabung.pack()

label_tinggi_tabung.pack()
entry_tinggi_tabung.pack()

label_jari_kerucut.pack()
entry_jari_kerucut.pack()

label_tinggi_kerucut.pack()
entry_tinggi_kerucut.pack()

label_jari_bola.pack()
entry_jari_bola.pack()

# Tombol untuk menghitung luas dan volume
button_hitung = tk.Button(app, text="Hitung Luas & Volume", command=hitung_luas_dan_volume)
button_hitung.pack()

# Widget Text untuk menampilkan hasil
entry_hasil_luas = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30)
entry_hasil_luas.pack()

entry_hasil_volume = tk.Entry(app,borderwidth=5, highlightthickness=4, width=30)
entry_hasil_volume.pack()



# Menjalankan aplikasi
app.mainloop()

