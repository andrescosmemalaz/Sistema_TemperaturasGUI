import tkinter as tk
from tkinter import ttk
import os
def funcion_click():
    accion.configure(text='**¡Haz hecho click!**')
    etiqueta.configure(foreground='red')
ventana = tk.Tk()
ventana.geometry('300x100+100+100')
ventana.title('Pythn -Tkinter')
etiqueta = ttk.Label(ventana, text='Hola a todos!!!')
etiqueta.grid(row=0, column=0)
# Agrega un boton
accion = ttk.Button(ventana, text='Haz click aquí', command=funcion_click)
accion.grid(column=1, row=0)
ventana.mainloop()
