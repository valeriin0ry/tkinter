from tkinter import *
from tkinter import messagebox as mb
from string import *
from tkinter import simpledialog as sd
from tkinter import simpledialog
import random
import imghdr
import smtplib
import ssl
def saada_email(receiver_email, subject, message):
    sender_email = "s1ncepr3m@gmail.com"
    password = simpledialog.askstring("Kood", "Sisesta oma 2FA kood:", show="*")
    if password is None:
        return  
    msg = f"Subject: {subject}\n{message}"
    try:
        context = ssl.create_default_context()
        smtp_server = "smtp.gmail.com"
        port = 587
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
        print("Email saadetud!")
    except Exception as e:
        print(f"Emaili saatmine ebaõnnestus. Viga: {str(e)}")
    finally:
        server.quit()

def registreeri_kasutaja():
    kasutajanimi = kasutajanime_sisestus.get()
    parool = parooli_sisestus.get()
    email = emaili_sisestus.get()

    with open("kasutajad.txt", "r") as f:
        kasutajad = f.readlines()

    kasutajad = [kasutaja.strip().split(",") for kasutaja in kasutajad]
    kasutajanimed = [kasutaja[0] for kasutaja in kasutajad]
    if kasutajanimi in kasutajanimed:
        mb.showerror("Registreerimine", "Kasutajanimi on juba võetud!")
        return

    if kasutajanimi and parool and email:  
        with open("kasutajad.txt", "a") as f:
            f.write(f"{kasutajanimi},{parool},{email}\n")
        saada_email(email, "Registreerimise kinnitus", f"Tere {kasutajanimi},\nTeid on edukalt registreeritud!")
        mb.showinfo("Registreerimine", "Kasutaja on edukalt registreeritud!")
    else:
        mb.showerror("Registreerimine", "Kasutajanimi, parool või e-post on puudu!")

def autoriseeri_kasutaja():
    kasutajanimi = kasutajanime_sisestus.get()
    parool = parooli_sisestus.get()

    with open("kasutajad.txt", "r") as f:
        kasutajad = f.readlines()

    kasutajad = [kasutaja.strip().split(",") for kasutaja in kasutajad]
    autoriseeritud = False
    for kasutaja in kasutajad:
        if kasutaja and len(kasutaja) >= 2 and kasutaja[0] == kasutajanimi and kasutaja[1] == parool:
            autoriseeritud = True
            break
        
    if autoriseeritud:
        mb.showinfo("Autoriseerimine", "Kasutaja on edukalt autoriseeritud!")
    else:
        mb.showerror("Autoriseerimine", "Vale kasutajanimi või parool!")

def muuda_parooli(vana_parool, uus_parool1, uus_parool2):
    kasutajanimi = kasutajanime_sisestus.get()

    with open("kasutajad.txt", "r") as f:
        kasutajad = f.readlines()

    if not kasutajad:
        mb.showerror("Parooli muutmine", "Kasutajaid ei leitud!")
        return

    kasutajad = [kasutaja.strip().split(",") for kasutaja in kasutajad]

    for i, kasutaja in enumerate(kasutajad):
        if kasutaja and len(kasutaja) >= 2 and kasutaja[0] == kasutajanimi:
            if kasutaja[1] == vana_parool and uus_parool1 == uus_parool2 and uus_parool1 != '':
                kasutajad[i][1] = uus_parool1
                with open("kasutajad.txt", "w") as f:
                    for kasutaja in kasutajad:
                        f.write(f"{kasutaja[0]},{kasutaja[1]}\n")
                saada_email(kasutaja[2], "Parooli muutmine", f"Tere {kasutajanimi},\nTeie uus parool on: {uus_parool1}")
                mb.showinfo("Parooli muutmine", "Parool on edukalt muudetud!")
                return
            else:
                mb.showerror("Parooli muutmine", "Vale parool või uued paroolid ei kattu või on tühjad!")
                return
    mb.showerror("Parooli muutmine", "Kasutajanime ei leitud!")

def loo_muuda_parooli_aken():
    muuda_parooli_aken = Toplevel(aken)
    muuda_parooli_aken.geometry("300x280")
    muuda_parooli_aken.title("Muuda parooli")

    muuda_parooli_aken.configure(bg="#C71585")
    raam = Frame(muuda_parooli_aken, bg="#C71585")
    raam.pack(pady=20)

    kasutaja_silt = Label(raam, text="Kasutajanimi:", bg="#C71585", fg="#800000")
    kasutaja_silt.grid(row=0, column=0, pady=5)
    kasutaja_entry = Entry(raam, bg="#C71585", fg="#800000", font="Times_New_Roman 14", width=25)
    kasutaja_entry.grid(row=0, column=1, pady=5)

    vana_parooli_silt = Label(raam, text="Vana parool:", bg="#C71585", fg="#800000")
    vana_parooli_silt.grid(row=1, column=0, pady=5)
    vana_parool_entry = Entry(raam, bg="#C71585", fg="#800000", font="Times_New_Roman 14", show="*", width=25)
    vana_parool_entry.grid(row=1, column=1, pady=5)

    uus_parool1_silt = Label(raam, text="Uus parool:", bg="#C71585", fg="#800000")
    uus_parool1_silt.grid(row=2, column=0, pady=5)
    uus_parool1_entry = Entry(raam, bg="#C71585", fg="#800000", font="Times_New_Roman 14", show="*", width=25)
    uus_parool1_entry.grid(row=2, column=1, pady=5)

    uus_parool2_silt = Label(raam, text="Korda uut parooli:", bg="#C71585", fg="#800000")
    uus_parool2_silt.grid(row=3, column=0, pady=5)
    uus_parool2_entry = Entry(raam, bg="#C71585", fg="#800000", font="Times_New_Roman 14", show="*", width=25)
    uus_parool2_entry.grid(row=3, column=1, pady=5)

    muuda_nupp = Button(raam, text="Muuda", bg="#CD5C5C", fg="white", font="Times_New_Roman 14", width=15, command=lambda: muuda_parooli(vana_parool_entry.get(), uus_parool1_entry.get(), uus_parool2_entry.get()))
    muuda_nupp.grid(row=4, columnspan=2, pady=5)

aken = Tk()
aken.geometry("500x400")
aken.title("Autoriseerimine ja registreerimine")
aken.configure(bg="#DC143C")
pealkiri = Label(aken,
                 text="Autoriseerimine ja registreerimine",
                 bg="#DC143C",
                 fg="#512512",
                 cursor="star",
                 font="Times_New_Roman 16",
                 justify="center",
                 height=3, width=26)
pealkiri.pack()

raam = Frame(aken, bg="#DC143C")
raam.pack(pady=20)

kasutajanime_silt = Label(raam, text="Kasutajanimi:", bg="#DC143C", fg="#512512")
kasutajanime_silt.grid(row=0, column=0, pady=5)
kasutajanime_sisestus = Entry(raam, bg="#C71585", fg="#512512", font="Times_New_Roman 16", width=25)
kasutajanime_sisestus.grid(row=0, column=1, pady=5)

parooli_silt = Label(raam, text="Parool:", bg="#DC143C", fg="#512512")
parooli_silt.grid(row=1, column=0, pady=5)
parooli_sisestus = Entry(raam, bg="#C71585", fg="#512512", font="Times_New_Roman 16", width=25, show="*")
parooli_sisestus.grid(row=1, column=1, pady=5)

emaili_silt = Label(raam, text="E-post:", bg="#DC143C", fg="#512512")
emaili_silt.grid(row=2, column=0, pady=5)
emaili_sisestus = Entry(raam, bg="#C71585", fg="#512512", font="Times_New_Roman 16", width=25)
emaili_sisestus.grid(row=2, column=1, pady=5)

registreeri_nupp = Button(raam, text="Registreeri", bg="#C71585", fg="#512512", font="Times_New_Roman 16", width=15, command=registreeri_kasutaja)
registreeri_nupp.grid(row=3, column=0, pady=5, padx=5)

autoriseeri_nupp = Button(raam, text="Autoriseeri", bg="#C71585", fg="#512512", font="Times_New_Roman 16", width=15, command=autoriseeri_kasutaja)
autoriseeri_nupp.grid(row=3, column=1, pady=5, padx=5)

muuda_parool_nupp = Button(raam, text="Muuda parool", bg="#C71585", fg="#512512", font="Times_New_Roman 16", width=15, command=loo_muuda_parooli_aken)
muuda_parool_nupp.grid(row=4, columnspan=2, pady=5)

def sulge_programm():
    aken.destroy()

sulge_nupp = Button(raam,
                    text="Sulge",
                    bg="#C71585",
                    fg="#512512",
                    font="Times_New_Roman 16",
                    width=15,
                    command=sulge_programm)

sulge_nupp.grid(row=5, columnspan=2, pady=5)

aken.mainloop()
