from tkinter import Frame, Label, Entry, Button, Tk, W, E, N, S, messagebox
from celcius import Celcius

class FrmCelcius:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, bg="#d9f7be")  # Warna latar belakang
        mainFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        Label(mainFrame, text='Celcius:', bg="#d9f7be").grid(row=0, column=0,
                                                            sticky=W, padx=5, pady=5)
        self.txtCelcius = Entry(mainFrame, font=("Arial", 12))
        self.txtCelcius.grid(row=0, column=1, padx=5, pady=5, sticky=E)

        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung, font=("Arial", 12))
        self.btnHitung.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        Label(mainFrame, text="Fahrenheit:", bg="#d9f7be").grid(row=1, column=0,
                                                               sticky=W, padx=5, pady=5)
        self.txtFahrenheit = Entry(mainFrame, state="readonly", font=("Arial", 12))
        self.txtFahrenheit.grid(row=1, column=1, padx=5, pady=5, sticky=E)

        Label(mainFrame, text="Kelvin:", bg="#d9f7be").grid(row=2, column=0,
                                                           sticky=W, padx=5, pady=5)
        self.txtKelvin = Entry(mainFrame, state="readonly", font=("Arial", 12))
        self.txtKelvin.grid(row=2, column=1, padx=5, pady=5, sticky=E)

        Label(mainFrame, text="Reamur:", bg="#d9f7be").grid(row=3, column=0,
                                                            sticky=W, padx=5, pady=5)
        self.txtReamur = Entry(mainFrame, state="readonly", font=("Arial", 12))
        self.txtReamur.grid(row=3, column=1, padx=5, pady=5, sticky=E)

    def onHitung(self):
        try:
            suhu_celcius = float(self.txtCelcius.get())
            C = Celcius(suhu_celcius)

            # Suhu dalam Fahrenheit
            F = C.get_fahrenheit()
            self.txtFahrenheit.config(state="normal")
            self.txtFahrenheit.delete(0, "end")
            self.txtFahrenheit.insert("end", str(F))
            self.txtFahrenheit.config(state="readonly")

            # Suhu dalam Kelvin
            K = C.get_kelvin()
            self.txtKelvin.config(state="normal")
            self.txtKelvin.delete(0, "end")
            self.txtKelvin.insert("end", str(K))
            self.txtKelvin.config(state="readonly")

            # Suhu dalam Reamur
            R = C.get_reamur()
            self.txtReamur.config(state="normal")
            self.txtReamur.delete(0, "end")
            self.txtReamur.insert("end", str(R))
            self.txtReamur.config(state="readonly")

        except ValueError:
            messagebox.showerror("Error", "Masukkan suhu yang valid")

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmCelcius(root, "Konversi Suhu Celcius")
    root.mainloop()