import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Matakuliah import Matakuliah

class FormMatakuliah:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='kodemk:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtkodemk = Entry(mainFrame) 
        self.txtkodemk.grid(row=0, column=1, padx=5, pady=5) 
        self.txtkodemk.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='namamk:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtnamamk = Entry(mainFrame) 
        self.txtnamamk.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='SKS:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtsks = Entry(mainFrame) 
        self.txtsks.grid(row=2, column=1, padx=5, pady=5) 

        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'kodemk', 'namamk','sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kodemk', text='kodemk')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='namamk')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='sks')
        self.tree.column('sks', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtkodemk.delete(0,END)
        self.txtkodemk.insert(END,"")
        self.txtnamamk.delete(0,END)
        self.txtnamamk.insert(END,"")
        self.txtsks.delete(0,END)  
        self.txtsks.insert(END, "")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data Matakuliah
        mtkh = Matakuliah()
        result = mtkh.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        kodemk = self.txtkodemk.get()
        mtkh = Matakuliah()
        res = mtkh.getBykodemk(kodemk)
        rec = mtkh.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtnamamk.focus()
        return res
        
    def TampilkanData(self, event=None):
        kodemk = self.txtkodemk.get()
        mtkh = Matakuliah()
        res = mtkh.getBykodemk(kodemk)
        self.txtnamamk.delete(0,END)
        self.txtnamamk.insert(END,mtkh.namamk)
        sks = mtkh.sks
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kodemk = self.txtkodemk.get()
        namamk = self.txtnamamk.get()
        sks = self.txtsks.get()
        
        self.onCari
        mtkh = Matakuliah()
        mtkh.kodemk = kodemk
        mtkh.namamk = namamk
        mtkh.sks = sks
        if(self.ditemukan==True):
            res = mtkh.updateBykodemk(kodemk)
            ket = 'Diperbarui'
        else:
            res = mtkh.simpan()
            ket = 'Disimpan'
            
        rec = mtkh.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtkodemk.get()
        self.onCari()
        mtkh = Matakuliah()
        mtkh.kodemk = kodemk
        if(self.ditemukan==True):
            res = mtkh.deleteBykodemk(kodemk)
            rec = mtkh.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMatakuliah(root, "Aplikasi Data Matakuliah")
    root.mainloop() 