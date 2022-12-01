from tkinter import *
import random
class Tanultosztaly:
    szam=None
    talalat=None

    def __init__(self):
        self.szam=0
        self.talalat=0

    def generalas(self):
        pass

    ablak=Tk()
    ablak.title('proba')
    ablak.minsize(200, 200)
    szoveg=Label(ablak,text="Tanult")
    szoveg.pack()
    generator=Button(ablak,text='GEN',command=generalas)
    generator.pack()