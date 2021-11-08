from tkinter import *
import tkinter.font as font
import math as mt

master = Tk()
master.title('Calculator')
master.geometry('300x380')
master['bg'] = 'white'

myFont = font.Font(size=15)

#SCREEN
e = Entry(master, width=24, borderwidth=0, fg='white')
e['font'] = myFont
e['bg'] = 'black'
e.grid(row=0, column=0, columnspan= 4, padx=20, pady=20)

def angka(nilai):
    sebelum = e.get()
    e.delete(0,END)
    e.insert(0, str(sebelum)+str(nilai))

def tambah():
    nomorAwal = e.get()
    global nAwal
    global mtk
    mtk = "penjumlahan"
    nAwal = int(nomorAwal)
    e.delete(0, END)

def kurang():
    nomorAwal = e.get()
    global nAwal
    global mtk
    mtk = "pengurangan"
    nAwal = int(nomorAwal)
    e.delete(0, END)
def bagi():
    nomorAwal = e.get()
    global nAwal
    global mtk
    mtk = "pembagian"
    nAwal = int(nomorAwal)
    e.delete(0, END)
def kali():
    nomorAwal = e.get()
    global nAwal
    global mtk
    mtk = "perkalian"
    nAwal = int(nomorAwal)
    e.delete(0, END)
def samadengan():
    nomorAkhir = e.get()
    e.delete(0,END)
    if mtk == 'penjumlahan':
        e.insert(0, nAwal + int(nomorAkhir))
    elif mtk == 'pengurangan':
        e.insert(0, nAwal - int(nomorAkhir))
    if mtk == 'pembagian':
        try:
            hitung = nAwal / int(nomorAkhir)
            e.insert(0, hitung)
        except ZeroDivisionError:
            e.insert(0, "Error!!!")
    if mtk == 'perkalian':
        e.insert(0, nAwal * int(nomorAkhir))
    

#TOMBOL ANGKA
btn0 = Button(master, text='0', padx=20, pady=20, command=lambda:angka(0))
btn1 = Button(master, text='1', padx=20, pady=20, command=lambda:angka(1))
btn2 = Button(master, text='2', padx=20, pady=20, command=lambda:angka(2))
btn3 = Button(master, text='3', padx=20, pady=20, command=lambda:angka(3))
btn4 = Button(master, text='4', padx=20, pady=20, command=lambda:angka(4))
btn5 = Button(master, text='5', padx=20, pady=20, command=lambda:angka(5))
btn6 = Button(master, text='6', padx=20, pady=20, command=lambda:angka(6))
btn7 = Button(master, text='7', padx=20, pady=20, command=lambda:angka(7))
btn8 = Button(master, text='8', padx=20, pady=20, command=lambda:angka(8))
btn9 = Button(master, text='9', padx=20, pady=20, command=lambda:angka(9))
#TOMBOL OPERAND
btnDvd = Button(master, text='/', padx=20, pady=20, command=bagi, bg='purple', fg='white')
btnTms = Button(master, text='x', padx=20, pady=20, command=kali, bg='purple', fg='white')
btnSub = Button(master, text='-', padx=20, pady=20, command=kurang, bg='purple', fg='white')
btnAdd = Button(master, text='+', padx=20, pady=20, command=tambah, bg='purple', fg='white')
btnEql = Button(master, text='=', padx=20, pady=20, command=samadengan, bg='purple', fg='white')


#GRID ROW 1
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btnDvd.grid(row=1,column=3)
#GRID ROW 2
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btnTms.grid(row=2,column=3)
#GRID ROW 3
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btnSub.grid(row=3,column=3)
#GRID ROW 4
btn0.grid(row=4,column=0)
btnEql.grid(row=4,column=1, columnspan=2, ipadx=37)
btnAdd.grid(row=4, column=3)

master.mainloop()