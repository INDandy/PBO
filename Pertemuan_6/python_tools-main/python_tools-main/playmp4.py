import tkinter as tk
from tkinter import Label
import cv2
from PIL import Image, ImageTk

class VideoPlayerApp:
    def __init__(self, master, video_source):
        self.master = master
        self.master.title("Video Player")

        # Inisialisasi video capture dari OpenCV
        self.video_source = video_source
        self.vid = cv2.VideoCapture(self.video_source)

        # Inisialisasi label untuk menampilkan frame video
        self.video_label = Label(master)
        self.video_label.pack()

        # Button play
        self.play_button = tk.Button(master, text="Play", command=self.play_video)
        self.play_button.pack(pady=10)

        # Button stop
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_video)
        self.stop_button.pack(pady=10)

    def play_video(self):
        # Baca frame pertama dari video
        ret, frame = self.vid.read()

        # Konversi frame OpenCV menjadi format Tkinter
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.config(image=imgtk)

            # Terus membaca dan menampilkan frame
            self.show_frame()
        else:
            print("End of video")

    def show_frame(self):
        # Baca frame dari video
        ret, frame = self.vid.read()

        if ret:
            # Konversi frame OpenCV menjadi format Tkinter
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.config(image=imgtk)

            # Perbarui frame setiap 10 milidetik (100 milliseconds)
            self.master.after(100, self.show_frame)
        else:
            print("End of video")

    def stop_video(self):
        # Hentikan video
        if self.vid.isOpened():
            self.vid.release()
            self.video_label.config(image="")

if __name__ == "__main__":
    # Ganti 'video.mp4' dengan path video MP4 yang ingin Anda tampilkan
    root = tk.Tk()
    app = VideoPlayerApp(root, video_source="python_tools-main/python_tools-main/video.mp4")
    root.mainloop()
