import tkinter as tk
from tkinter import ttk
def funcion_click():
    accion.configure(text='Hola ' + nombre.get())
# get() obtiene el valor ingresado
# Inicializar ventana
ventana = tk.Tk()
ventana.geometry('300x100+100+100')
ventana.title("Python - Tkinter")
# Agregar etiqueta por medio de un objeto
etiqueta = ttk.Label(ventana, text="Escribe tu nombre")
etiqueta.grid(column=0, row=0)
# Agregar una caja de texto
nombre = tk.StringVar() # se crea la variable para Entry con StringVar
preguntar_nombre = ttk.Entry(ventana, width=20, textvariable=nombre)
preguntar_nombre.grid(column=0, row=1)
# Agregar un botón
accion = ttk.Button(ventana, text="Haz click aquí", command=funcion_click)
accion.grid(row=1, column=1)
ventana.mainloop()

