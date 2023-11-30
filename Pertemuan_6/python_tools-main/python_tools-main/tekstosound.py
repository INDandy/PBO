from gtts import gTTS 
from playsound import playsound
import tkinter as tk

class TextkeSuara:
    def __init__(self,master):
        self.master = master
        self.master.title = ("Teks Ke Suara")

        self.convert_button = tk.Button(master, text="Menyuarakan", command=self.konversiteks)
        self.convert_button.pack(pady=5)
    def konversiteks(self):
        mytext = 'Dandy Royyan Firdaus, Kelas R1. NIM dua dua kosong lima satu satu kosong lima enam'
        language = 'id'
        myobj = gTTS(text=mytext, lang=language, slow=False)

        myobj.save("output.mp3")
        playsound("output.mp3")

if __name__=="__main__":
    root=tk.Tk()
    app = TextkeSuara(root)
    root.mainloop()