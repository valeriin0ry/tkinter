from tkinter import *
from tkinter import messagebox as mb
from string import *
from time import sleep
from tkinter import simpledialog as sd
import random
import imghdr
def registreeri_kasutaja():
    kasutajanimi = kasutajanime_sisestus.get()
    parool = parooli_sisestus.get()

    if kasutajanimi and parool:  
        with open("kasutajad.txt", "a") as f:
            f.write(f"{kasutajanimi},{parool}\n")
        mb.showinfo("Registreerimine", "Kasutaja on edukalt registreeritud!")
    else:
        mb.showerror("Registreerimine", "Kasutajanimi või parool on puudu!")

def autoriseeri_kasutaja():
    kasutajanimi = kasutajanime_sisestus.get()
    parool = parooli_sisestus.get()

    with open("kasutajad.txt", "r") as f:
        kasutajad = f.readlines()

    kasutajad = [kasutaja.strip().split(",") for kasutaja in kasutajad]
    if [kasutajanimi, parool] in kasutajad:
        mb.showinfo("Autoriseerimine", "Kasutaja on edukalt autoriseeritud!")
    else:
        mb.showerror("Autoriseerimine", "Vale kasutajanimi või parool!")

def muuda_parooli():
    vana_parool = vana_parool_entry.get()
    uus_parool1 = uus_parool1_entry.get()
    uus_parool2 = uus_parool2_entry.get()

    kasutajanimi = kasutajanime_sisestus.get()

    with open("kasutajad.txt", "r") as f:
        kasutajad = f.readlines()

    kasutajad = [kasutaja.strip().split(",") for kasutaja in kasutajad]

    for i, kasutaja in enumerate(kasutajad):
        if kasutaja and len(kasutaja) >= 2 and kasutaja[0] == kasutajanimi:
            if kasutaja[1] == vana_parool and uus_parool1 == uus_parool2 and uus_parool1 != '':
                kasutajad[i][1] = uus_parool1
                with open("kasutajad.txt", "w") as f:
                    for kasutaja in kasutajad:
                        f.write(f"{kasutaja[0]},{kasutaja[1]}\n")
                mb.showinfo("Parooli muutmine", "Parool on edukalt muudetud!")
                muuda_parooli_aken.destroy()
                return
            else:
                mb.showerror("Parooli muutmine", "Vale parool või uued paroolid ei kattu või on tühjad!")
                return
    mb.showerror("Parooli muutmine", "Kasutajanime ei leitud!")

def loo_muuda_parooli_aken():
    global muuda_parooli_aken, vana_parool_entry, uus_parool1_entry, uus_parool2_entry
    muuda_parooli_aken = Toplevel(aken)
    muuda_parooli_aken.geometry("300x200")
    muuda_parooli_aken.title("Muuda parooli")

    vana_parooli_silt = Label(muuda_parooli_aken, text="Vana parool:")
    vana_parooli_silt.pack()
    vana_parool_entry = Entry(muuda_parooli_aken, show="*")
    vana_parool_entry.pack()

    uus_parool1_silt = Label(muuda_parooli_aken, text="Uus parool:")
    uus_parool1_silt.pack()
    uus_parool1_entry = Entry(muuda_parooli_aken, show="*")
    uus_parool1_entry.pack()

    uus_parool2_silt = Label(muuda_parooli_aken, text="Korda uut parooli:")
    uus_parool2_silt.pack()
    uus_parool2_entry = Entry(muuda_parooli_aken, show="*")
    uus_parool2_entry.pack()

    muuda_nupp = Button(muuda_parooli_aken, text="Muuda", command=muuda_parooli)
    muuda_nupp.pack()

aken = Tk()
aken.geometry("500x370")
aken.title("Akna pealkiri")
aken.configure(bg="#DC143C")
aken.iconbitmap("icon.ico")

pealkiri = Label(aken,
                 text="Põhielemendid",
                 bg="#DC143C",
                 fg="#512512",
                 cursor="star",
                 font="Times_New_Roman 16",
                 justify="center",
                 height=3, width=26)

raam = Frame(aken, bg="#DC143C")

kasutajanime_silt = Label(raam, text="Kasutajanimi:", bg="#DC143C", fg="#512512")
parooli_silt = Label(raam, text="Parool:", bg="#DC143C", fg="#512512")
kasutajanime_sisestus = Entry(raam,
                              bg="#C71585",
                              fg="#512512",
                              font="Times_New_Roman 16",
                              width=20)
parooli_sisestus = Entry(raam,
                         bg="#C71585",
                         fg="#512512",
                         font="Times_New_Roman 16",
                         width=20,
                         show="*")
registreeri_nupp = Button(raam,
                          text="Registreeri",
                          bg="#C71585",
                          fg="#512512",
                          font="Times_New_Roman 16",
                          width=15,
                          command=registreeri_kasutaja)
autoriseeri_nupp = Button(raam,
                          text="Autoriseeri",
                          bg="#C71585",
                          fg="#512512",
                          font="Times_New_Roman 16",
                          width=15,
                          command=autoriseeri_kasutaja)
muuda_parool_nupp = Button(raam,
                           text="Muuda parool",
                           bg="#C71585",
                           fg="#512512",
                           font="Times_New_Roman 16",
                           width=15,
                           command=loo_muuda_parooli_aken)

def sulge_programm():
    aken.destroy()

sulge_nupp = Button(raam,
                    text="Sulge",
                    bg="#C71585",
                    fg="#512512",
                    font="Times_New_Roman 16",
                    width=15,
                    command=sulge_programm)

sulge_nupp.grid(row=4, columnspan=2, pady=5)
pealkiri.pack()
raam.pack(pady=20)
kasutajanime_silt.grid(row=0,column=0, pady=5)
kasutajanime_sisestus.grid(row=0,column=1, pady=5)
parooli_silt.grid(row=1,column=0, pady=5)
parooli_sisestus.grid(row=1,column=1, pady=5)
registreeri_nupp.grid(row=2,column=0, pady=5, padx=5)
autoriseeri_nupp.grid(row=2,column=1, pady=5, padx=5)
muuda_parool_nupp.grid(row=3,columnspan=2, pady=5)

aken.mainloop()