import tkinter as tk

def konversi_suhu():
    try:
        suhu_input = float(entry_suhu.get())
        jenis_konversi_from = var_from.get()
        jenis_konversi_to = var_to.get()

        if jenis_konversi_from == jenis_konversi_to:
            hasil = suhu_input
            unit_hasil.set(jenis_konversi_to)
            status_suhu = "Suhu Biasa"
        elif jenis_konversi_from == "Celsius" and jenis_konversi_to == "Fahrenheit":
            hasil = (suhu_input * 9/5) + 32
            unit_hasil.set("Fahrenheit")
            status_suhu = "Panas" if hasil > suhu_input else "Dingin"
        elif jenis_konversi_from == "Fahrenheit" and jenis_konversi_to == "Celsius":
            hasil = (suhu_input - 32) * 5/9
            unit_hasil.set("Celsius")
            status_suhu = "Panas" if hasil > suhu_input else "Dingin"
        elif jenis_konversi_from == "Celsius" and jenis_konversi_to == "Kelvin":
            hasil = suhu_input + 273.15
            unit_hasil.set("Kelvin")
            status_suhu = "Panas" if hasil > suhu_input else "Dingin"
        elif jenis_konversi_from == "Kelvin" and jenis_konversi_to == "Celsius":
            hasil = suhu_input - 273.15
            unit_hasil.set("Celsius")
            status_suhu = "Panas" if hasil > suhu_input else "Dingin"
        elif jenis_konversi_from == "Kelvin" and jenis_konversi_to == "Fahrenheit":
            hasil = (suhu_input - 273.15) * 9/5 + 32
            unit_hasil.set("Fahrenheit")
            status_suhu = "Panas" if hasil > suhu_input else "Dingin"
        else:
            hasil = suhu_input
            unit_hasil.set("Suhu")
            status_suhu = "Suhu Biasa"

        label_hasil.config(text=f"Hasil: {hasil:.2f} {unit_hasil.get()}\nStatus Suhu: {status_suhu}")
    except ValueError:
        label_hasil.config(text="Masukkan suhu dalam bentuk angka.")

# Membuat jendela utama
app = tk.Tk()
app.title("Konversi Suhu")

# Membuat elemen-elemen GUI
frame_input = tk.Frame(app, bd=5, relief=tk.GROOVE)
frame_input.pack(padx=10, pady=10)

label_suhu = tk.Label(frame_input, text="Masukkan Suhu:")
label_suhu.grid(row=0, column=0, padx=10, pady=10)

entry_suhu = tk.Entry(frame_input)
entry_suhu.grid(row=0, column=1, padx=10, pady=10)

label_from = tk.Label(frame_input, text="Dari:")
label_from.grid(row=1, column=0, padx=10, pady=10)

options_from = ["Celsius", "Fahrenheit", "Kelvin"]
var_from = tk.StringVar()
var_from.set(options_from[0])  # Set nilai default
dropdown_from = tk.OptionMenu(frame_input, var_from, *options_from)
dropdown_from.grid(row=1, column=1, padx=10, pady=5)

label_to = tk.Label(frame_input, text="Ke:")
label_to.grid(row=2, column=0, padx=10, pady=10)

options_to = ["Celsius", "Fahrenheit", "Kelvin"]
var_to = tk.StringVar()
var_to.set(options_to[0])  # Set nilai default
dropdown_to = tk.OptionMenu(frame_input, var_to, *options_to)
dropdown_to.grid(row=2, column=1, padx=10, pady=5)

button_konversi = tk.Button(frame_input, text="Konversi", command=konversi_suhu)
button_konversi.grid(row=3, column=0, columnspan=2, pady=10)

# Membuat elemen GUI untuk menampilkan hasil
frame_hasil = tk.Frame(app, bd=5, relief=tk.GROOVE)
frame_hasil.pack(padx=10, pady=10)

label_hasil = tk.Label(frame_hasil, text="Hasil:")
label_hasil.grid(row=0, column=0, pady=10)

unit_hasil = tk.StringVar()
unit_hasil.set("Suhu")

# Menjalankan aplikasi
app.mainloop()
