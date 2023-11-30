import tkinter as tk
from PIL import Image, ImageTk
import pytesseract

class TextFromImageApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text from Image")

        # Label untuk menampilkan gambar
        self.image_label = tk.Label(master)
        self.image_label.pack(pady=10)

        # Path gambar default
        self.default_image_path = "python_tools-main\python_tools-main\images\gambar4.png"

        # Menampilkan gambar di label
        image = Image.open(self.default_image_path)
        image = image.resize((300, 300))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

        # Entry untuk menampilkan teks
        self.text_entry = tk.Entry(master, width=40)
        self.text_entry.pack(pady=10)

        # Button untuk mendapatkan teks dari gambar
        self.get_text_button = tk.Button(master, text="Get Text", command=self.get_text_from_image)
        self.get_text_button.pack(pady=5)

    def get_text_from_image(self):
        # Menggunakan pytesseract untuk mendapatkan teks dari gambar
        image = Image.open(self.default_image_path)
        text = pytesseract.image_to_string(image)

        # Menampilkan teks di entry
        self.text_entry.delete(0, tk.END)
        self.text_entry.insert(0, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextFromImageApp(root)
    root.mainloop()
