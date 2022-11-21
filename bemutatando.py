from tkinter import *
import sajat_modul

p=sajat_modul.osztaly()

ablak = Tk()
ablak.title("Játék")
ablak.minsize(200,100)
szoveg=Label(ablak,text="Kitalálós játék")
submitbtn= Button(ablak, text="Submit", activebackground="red", activeforeground="blue", command=p.kitalalas).place(x=30, y=170)
nev = Entry(ablak).place(x=80, y=50)
p.name=str(nev.set())
proba = Entry(ablak).place(x=80, y=90)
p.tries=int(nev.set())
szam = Entry(ablak).place(x=95, y=130)
p.numbers=int(nev.set())
mainloop()
