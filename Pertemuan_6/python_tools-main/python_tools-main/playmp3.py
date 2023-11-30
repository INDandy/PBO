import tkinter as tk
import pygame
from tkinter.filedialog import askopenfilename
from tkinter import Label



class MusicPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")

        # Inisialisasi pygame mixer
        pygame.mixer.init()

        # Button play
        self.play_button = tk.Button(master, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        # Button stop
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.grid = Label(master, text="File: ")
        self.grid.pack(pady=5)

    def play_music(self):
        # Lokasi file musik
        music_file = "python_tools-main/python_tools-main/musik.mp3"

        # Load dan mainkan musik
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()

        self.grid.config(text="File: " + music_file)

    def stop_music(self):
        # Hentikan musik
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
