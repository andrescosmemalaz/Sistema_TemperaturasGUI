import tkinter as tk
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def btPres(x):
    etiqueta.configure(text='Botón {} presionado'.format(alfabeto[x]))

raiz = tk.Tk()
raiz.geometry('480x100+100+100')
raiz.title("Identificar botón presionado")

etiqueta = tk.Label(font=('Calibri', 12))
etiqueta.grid(row=1, column=0, columnspan=26)
botones = [0] * 26 # crea una lista de 26 botones

for i in range(26):
    botones[i] = tk.Button(text=alfabeto[i], command=lambda x=i: btPres(x))
    botones[i].grid(row=0, column=i)

raiz.mainloop()
