from module1 import *
salasõnad=[]
kasutajanimed=[]
while True:
    print("1 - registreerimine\n2 - autoriseerimine\n3 - nime või parooli muutmine\n4 - unustanud parooli taastamine\n5 - lõpetamine")
    vastus=input("Sisestage arv: ")
    if vastus=="1":
        print("Registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus=="2":
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus == "3":
        print("Nime või parooli muutmine")
        vastus = input("Kas muudame nime või parooli?: ")
        if vastus == "nimi":
            kasutajanimed = nimi_või_parooli_muurmine(kasutajanimed, "nimi")
        elif vastus == "parool":
            salasõnad = nimi_või_parooli_muurmine(salasõnad, "parool")
        elif vastus == "mõlemad":
            kasutajanimed = nimi_või_parooli_muurmine(kasutajanimed, "nimi")
            salasõnad = nimi_või_parooli_muurmine(salasõnad, "parool")
    elif vastus=="4":
        print("Unustanud parooli taastamine")
        parooli_taastamine(kasutajanimed, salasõnad)
    elif vastus=="5":
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")
