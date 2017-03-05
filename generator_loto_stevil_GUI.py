# -*- coding: utf-8 -*-
from random import randint as nakljucna_stevilka
import Tkinter
import tkMessageBox

lotto_stevilke = []
def ustvari_lotto_stevilke(stevilo_stevilk):
    return [nakljucna_stevilka(1,39) for i in range(stevilo_stevilk) if i not in lotto_stevilke]

def stevilo_listkov():
    return int(vnos1.get())

def ustvari_lotto_list():
    stevilo_stevilk = int(vnos2.get())
    for i in range(stevilo_listkov()):
        lotto_list = ustvari_lotto_stevilke(stevilo_stevilk)
        lotto_stevilke.append(lotto_list)

    for i in lotto_stevilke:
        i.sort()
        tkMessageBox.showinfo("Vaše srečne številke so:", i )

glavno_okno = Tkinter.Tk()
glavno_okno.title("Dobrodošli v programu za generiranje Loto številk!")
glavno_okno.geometry("600x400+500+300")

skupina1 = Tkinter.Frame(glavno_okno)
skupina1.pack(side=Tkinter.TOP)

oznaka1 = Tkinter.Label(skupina1, text="Prosimo vnesite število listkov:")
oznaka1.config(font=("Consolas", 14, "bold"))
oznaka1.pack()

vnos1 = Tkinter.Entry(skupina1)
vnos1.pack()

oznaka2 = Tkinter.Label(skupina1, text="Prosimo vnesite število številk:")
oznaka2.config(font=("Consolas", 14, "bold"))
oznaka2.pack()

vnos2 = Tkinter.Entry(skupina1)
vnos2.pack()

gumb = Tkinter.Button(skupina1, text="Ustvari lotto številke!", command=ustvari_lotto_list)
gumb.pack()

glavno_okno.mainloop()