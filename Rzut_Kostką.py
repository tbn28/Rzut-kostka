import random
import sys
import os
import tkinter
from tkinter import *
from tkinter import messagebox

main = tkinter.Tk()
main.title("Rzut kostka")
main.geometry("480x360")
main.configure(background="#E6DC9E")

def koniec():
    main.destroy()

rzuca1Label = Label(main, text = "Imie pierwszego gracza", bg = "#6A97F7", font=("Comic Sans MS",14,"bold"), foreground="white")
rzuca1 = Entry(main, bg = "#DBD1C8", font=("Comic Sans MS",14,"bold"))
rzuca2Label = Label(main, text = "Imie drugiego gracza", bg = "#6A97F7", font=("Comic Sans MS",14,"bold"), foreground="white")
rzuca2 = Entry(main, bg = "#DBD1C8", font=("Comic Sans MS",14,"bold"))

nLabel = Label(main, text = "Ilosc tur", bg = "#EDA258", font=("Comic Sans MS",14,"bold"), foreground="white")
n = Entry(main, bg = "#DBD1C8", font=("Comic Sans MS",14,"bold"))

rzuca1Label.pack()
rzuca1.pack()
rzuca2Label.pack()
rzuca2.pack()
nLabel.pack()
n.pack()

def losowanie():
    return random.randint(1,6)

def begingame():
    global rzuca1, rzuca2, n

    liczzw1 = 0
    liczzw2 = 0

    liczba_tur = int(n.get())
    nickname1 = str(rzuca1.get())
    nickname2 = str(rzuca2.get())

    tura = 1

    while (tura <= liczba_tur or liczzw1 == liczzw2):
        text = ""

        text += "Runda numer " + str(tura) + "\n"  + "\n"

        text += "Rzuca " + nickname1 + "\n"  + "\n"

        rzut1 = losowanie()
        rzut2 = losowanie()
        sum1 = rzut1 + rzut2

        text += "Pierwszy rzut : " + str(rzut1) + "\n"
        text += "Drugi rzut    : " + str(rzut2) + "\n"
        text += "Laczny wynik : " + str(sum1) + "\n"  + "\n"
        text += "Rzuca " + nickname2 + "\n"  + "\n"

        rzut1 = losowanie()
        rzut2 = losowanie()
        sum2 = rzut1 + rzut2

        text += "Pierwszy rzut : " + str(rzut1) + "\n"
        text += "Drugi rzut    : " + str(rzut2) + "\n"
        text += "Laczny wynik : " + str(sum2) + "\n"
        text += "\n"

        if sum1 > sum2:
            text += "Runde wygral gracz " + nickname1 + "\n"
            liczzw1 += 1
        elif sum1 < sum2:
            text += "Runde wygral gracz " + nickname2 + "\n"
            liczzw2 += 1
        else:
            text += "Mamy remis" + "\n"

        text += "\n" + "Wcisnij OK aby kontynuowac..."

        messagebox.showinfo('Rzut kostka', text)

        tura += 1

    if liczzw1 > liczzw2:
        messagebox.showinfo('Rzut kostka', "Mecz wygral gracz " + nickname1 + " z wynikiem " + str(liczzw1) + " do " + str(liczzw2))
    elif liczzw1 < liczzw2:
        messagebox.showinfo('Rzut kostka', "Mecz wygral gracz " + nickname2 + " z wynikiem " + str(liczzw2) + " do " + str(liczzw1))
##    else:
##        messagebox.showinfo('Rzut kostka', "Nikt nie wygral! Wynik to " + str(liczzw1) + " do " + str(liczzw2))

l = tkinter.Label(main, text = "Zagrajmy w gre !", bg = "#CC3333", font=("Comic Sans MS",18,"bold"), foreground="white")
l1 = tkinter.Label(main, text = "Aby rozpoczac kliknij ponizej ", bg = "green", font=("Comic Sans MS",10,"bold"))
b = tkinter.Button(main, text = "Rozpocznij nowa gre !", bg = "#B1DE6F", font=("Comic Sans MS",18,"bold"), foreground="white", command = begingame)
b1 = tkinter.Button(main, text = "Wyjdz z programu", fg = "red", bg = "#111742", font=("Comic Sans MS",12,"bold"), foreground="white", command = koniec)

l.pack()
l1.pack(fill = X)
b.pack()
b1.pack(side = BOTTOM)

main.mainloop()


