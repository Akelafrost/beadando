from tkinter import *
import sajat_modul

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
    kitalalas.mainloop()
p=sajat_modul.osztaly()

ablak = Tk()
ablak.title("Játék")
ablak.minsize(200,200)
szoveg=Label(ablak,text="Kitalálós játék")
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
