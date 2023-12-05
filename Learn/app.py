#na githubu nebude fungovat protože musíš mít stahlé pygame 

import tkinter as tk
window = tk.Tk()

window.title("Kalkulačka")
window.geometry("350x500")

""""
label = tk.Label(
    text="Ahoj",
    font=("Times 15"),
    fg="white",  # Nastavení barvy písma
    bg="black",  # Nastavení barvy pozadí 
    width=10,
    height=2,
)
label.pack() #pack = umístení objektu
"""

greeting = tk.Label(window, text="Převodník", font=("Times 15"))

def prevadej():
    m = float(metry.get())
    ft = m / 0.3048
    stopy.delete(0, "end")
    stopy.insert(0, ft)

metry = tk.Entry(width=25, font=("Times 15"),)
prevod = tk.Button(window, text="Převod", font=("Times 15"), command=prevadej)
stopy = tk.Entry(width=25, font=("Times 15"),)

greeting.pack()
metry.pack()
prevod.pack()
stopy.pack()

window.mainloop()