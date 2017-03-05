# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox

naloge = {}

def main():
    n = vnos.get()
    status = vnos2.get()
    if status == "da":
        naloge[n] = True
    else:
        naloge[n] = False

def prikaz_nalog():
    for n in naloge:
        if naloge[n] is True:
            tkMessageBox.showinfo("Opravljene naloge:", n)
    for n in naloge:
        if naloge[n] is False:
            tkMessageBox.showerror("Neopravljene naloge:", n)

glavno_okno = Tkinter.Tk()
glavno_okno.title("Dobrodošli v TODO task management")
glavno_okno.geometry("600x400+500+300")

skupina1 = Tkinter.Frame(glavno_okno)
skupina1.pack(side=Tkinter.TOP)

oznaka = Tkinter.Label(skupina1, text="Prosimo vnesite nalogo in status", fg="black", bg="yellow")
oznaka.config(font=("Consolas", 20, "bold"))
oznaka.pack()

vnos = Tkinter.Entry(skupina1)
vnos.pack()

vnos2 = Tkinter.Entry(skupina1)
vnos2.pack()

gumb = Tkinter.Button(skupina1, text="Vnesi!", command=main)
gumb.pack()

gumb2 = Tkinter.Button(skupina1, text="Prikaži naloge!", command=prikaz_nalog)
gumb2.pack()

glavno_okno.mainloop()