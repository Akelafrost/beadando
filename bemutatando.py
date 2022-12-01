from tkinter import *
import sajat_modul

def fajliras():
    nev=str(p.name)
    proba=str(p.tries)
    szam=str(p.number)
    megoldas=str(p.guessesLeft)
    with open('fajl.txt', "w", encoding='utf-8') as fajl:
        if p.guessesLeft != 0:
            sor ='A'+nev+'nevű játékos'+proba+'probálkozásból'+megoldas+' próbálkozás alatt megfejtette a számot ami'+szam+'az'
        else:
            sor = 'A' + nev + 'nevű játékos nem sikerült kitalálnia'
    fajl.write(sor)


def kiiras():

    p.name = str(hossznev.get())
    p.tries = int(hosszproba.get())
    p.numbers = int(hosszszam.get())
    kitalalas=Toplevel(ablak)
    kitalalas.geometry('400x400')
    kitalalas.title('Kitalálás')
    kitalalasszoveg=Label(kitalalas,text='Irj egy számot!')
    kitalalasszoveg.grid(row=0,column=0)
    szam = IntVar(ablak,value=1)
    talal = Entry(kitalalas,textvariable=szam, width=5)
    talal.grid(row=1, column=1, sticky=W)
    p.guess=int(talal.get())
    ok = Button(kitalalas, text='OK', command=p.kitalalas, width=3, height=1)
    ok.grid(row=2,column=2, sticky=E)
    szamgenerator = Button(kitalalas, text='Generator', command=p.szam, width=30, height=1)
    szamgenerator.grid(row=2, column=3, sticky=E)
    fajlbairas=Button(kitalalas,text='iras',command=fajliras)
    fajlbairas.grid(row=3, column=1)
    kitalalas.mainloop()
p=sajat_modul.osztaly()

ablak = Tk()
ablak.title("Játék")
ablak.minsize(200,200)
szoveg=Label(ablak,text="Kitalálós játék")
szoveg.grid(row=1,column=1)
submitbtn= Button(ablak, text="Submit", activebackground="red", activeforeground="blue", command=kiiras).place(x=30, y=170)
nev = StringVar(ablak,value='jatekos')
hossznev = Entry(ablak,textvariable=nev)
hossznev.grid(row=2, column=2, sticky=W)

hosszproba = Entry(ablak, width=15)
hosszproba.insert(0,'5')
hosszproba.grid(row=3, column=2, sticky=W)


hosszszam = Entry(ablak, width=15)
hosszszam.insert(0,'50')
hosszszam.grid(row=4, column=2, sticky=W)

mainloop()
