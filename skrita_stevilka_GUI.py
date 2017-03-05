# -*- coding: utf-8 -*-
import random
import Tkinter
import tkMessageBox

def main():
    skrita_stevilka = random.randint(1, 100)
    ugibana_stevilka = int(vnos.get())
    if skrita_stevilka != ugibana_stevilka:
        ugibana_stevilka = int(vnos.get())
        tkMessageBox.showerror("Napačno!", "Vstavite 5€ in poizkusite ponovno")
    else:
        tkMessageBox.showinfo("Čestitamo!", "Zadeli ste 1000€!")

glavno_okno = Tkinter.Tk()
glavno_okno.title("Dobrodošli v igri ugani skrito številko!")
glavno_okno.geometry("600x400+500+300")

skupina1 = Tkinter.Frame(glavno_okno)
skupina1.pack(side=Tkinter.TOP)

oznaka = Tkinter.Label(skupina1, text="Prosimo vnesite številko med 1 in 100:", fg="black", bg="yellow")
oznaka.config(font=("Consolas", 20, "bold"))
oznaka.pack()

vnos = Tkinter.Entry(skupina1)
vnos.pack()

gumb = Tkinter.Button(skupina1, text="Poizkusi srečo!", command=main)
gumb.pack()

glavno_okno.mainloop()