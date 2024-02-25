import tkinter as tk
from tkinter import Menu, messagebox
from FrmLogin import FormLogin
from FrmPersegi import FrmPersegi
from FrmSegitiga import FrmSegitiga
from FrmLingkaran import FrmLingkaran

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Menu Demo')
        self.root.geometry("900x400")
        self.__data = None
        self.__level = None
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar)
        self.admin_menu = Menu(self.menubar)
        self.mahasiswa_menu = Menu(self.menubar)
        self.dosen_menu = Menu(self.menubar)

        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.file_menu.add_command(label='Exit', command=self.root.destroy)

        self.admin_menu.add_command(label='Admin-1', command=lambda: self.new_window("Luas Persegi", FrmPersegi))
        self.admin_menu.add_command(label='Admin-2', command=lambda: self.new_window("Luas Segitiga", FrmSegitiga))
        self.admin_menu.add_command(label='Admin-3', command=lambda: self.new_window("Luas Lingkaran", FrmLingkaran))

        self.mahasiswa_menu.add_command(label='Mahasiswa-1', command=lambda: self.new_window("Luas Persegi", FrmPersegi))
        self.mahasiswa_menu.add_command(label='Mahasiswa-2', command=lambda: self.new_window("Luas Segitiga", FrmSegitiga))
        self.mahasiswa_menu.add_command(label='Mahasiswa-3', command=lambda: self.new_window("Luas Lingkaran", FrmLingkaran))

        self.dosen_menu.add_command(label='Dosen-1', command=lambda: self.new_window("Luas Persegi", FrmPersegi))
        self.dosen_menu.add_command(label='Dosen-2', command=lambda: self.new_window("Luas Segitiga", FrmSegitiga))
        self.dosen_menu.add_command(label='Dosen-3', command=lambda: self.new_window("Luas Lingkaran", FrmLingkaran))

        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def new_window(self, number, _class):
        new = tk.Toplevel(self.root)
        new.transient()
        new.grab_set()
        _class(new, number, self.update_main_window)

    def update_main_window(self, data):
        self.__data = data
        level = self.__data[0]
        login_valid = self.__data[1]
        if login_valid:
            messagebox.showinfo("Login Berhasil", f"Selamat Datang, {level}!")
            index = self.file_menu.index('Login')
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Logout', command=self.Logout)

            if level == 'admin':
                self.menubar.add_cascade(label="Admin", menu=self.admin_menu)
                self.__level = 'Admin'
            elif level == 'mahasiswa':
                self.menubar.add_cascade(label="Mahasiswa", menu=self.mahasiswa_menu)
                self.__level = 'Mahasiswa'
            elif level == 'dosen':
                self.menubar.add_cascade(label="Dosen", menu=self.dosen_menu)
                self.__level = 'Dosen'
            else:
                pass

    def Logout(self):
        index = self.file_menu.index('Logout')
        self.file_menu.delete(index)
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.remove_all_menus()

    def remove_all_menus(self):
        index = self.menubar.index(self.__level)
        if index is not None:
            self.menubar.delete(index)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()