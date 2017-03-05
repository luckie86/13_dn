# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox

def main():
    if vnos.get() > 0 and vnos.get().isdigit():
        kilometri = int(vnos.get())
        kilometri_v_milje = kilometri * 0.621371192
        tkMessageBox.showinfo("%s kilometrov znaša: " % (kilometri), "%s milj" %(kilometri_v_milje))
    else:
        tkMessageBox.showerror("Napačno!", "Prosimo vnesite samo številke")

glavno_okno = Tkinter.Tk()
glavno_okno.title("Dobrodošli v pretvornik kilometrov v milje")
glavno_okno.geometry("600x400+500+300")

skupina1 = Tkinter.Frame(glavno_okno)
skupina1.pack(side=Tkinter.TOP)

oznaka = Tkinter.Label(skupina1, text="Prosimo vnesite število kilometrov", fg="black", bg="yellow")
oznaka.config(font=("Consolas", 20, "bold"))
oznaka.pack()

vnos = Tkinter.Entry(skupina1)
vnos.pack()

gumb = Tkinter.Button(skupina1, text="Pretvori!", command=main)
gumb.pack()

glavno_okno.mainloop()
