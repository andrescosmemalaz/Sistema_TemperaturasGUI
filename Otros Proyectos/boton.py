import tkinter as tk
from tkinter import ttk

def funcion_click():
    respuesta = ttk.Label(ventana,text= opcion.get())
    respuesta.grid(column=1, row=3)

ventana = tk.Tk()
ventana.geometry('300x100')
ventana.title('Python-Tkinter')

etiqueta = ttk.Label(ventana, text='Selecciona una opcion')
etiqueta.grid(column=0,row=0)
opcion = tk.StringVar()
seleccionar_opcion = ttk.Combobox(ventana, width=12, textvariable=opcion)
seleccionar_opcion['values'] = ('SI','NO')
seleccionar_opcion.grid(column=0,row=1)
seleccionar_opcion.current(0)
accion = ttk.Button(ventana, text='OK',command=funcion_click)
accion.grid(row=1, column=1)

ventana.mainloop()
