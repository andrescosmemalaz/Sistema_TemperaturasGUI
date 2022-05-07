import tkinter as tk
from tkinter import ttk
def funcion_click():
    respuesta = ttk.Label(ventana, text='Seleccionado el ' + numero.get())
    respuesta.grid(column=1, row=3)

ventana = tk.Tk()
ventana.geometry('300x100+100+100')
ventana.title("Python - Tkinter")
etiqueta = ttk.Label(ventana, text="Selecciona un número")
etiqueta.grid(column=0, row=0)
# Agregar lista desplegable
numero = tk.StringVar()
seleccionar_numero = ttk.Combobox(ventana, width=12, textvariable=numero,state='readonly')
# Llenar lista desplegable
seleccionar_numero['values'] = (1, 3, 5, 7, 11)
# Posicionar lista desplegable
seleccionar_numero.grid(column=0, row=1)
# Elemento de la lista seleccionado por default
seleccionar_numero.current(0)
accion = ttk.Button(ventana, text="Ok", command=funcion_click)
accion.grid(row=1, column=1)

ventana.mainloop()