import tkinter as tk
ventana = tk.Tk()
ventana.geometry('300x100+100+100')
ventana.title('Uso de Etiquetas')
#Creamos Las etiquetas y le damos su ubicación con grid
labelUsuario = tk.Label(text='Usuario')
labelUsuario.grid(row=0, column=0, sticky=tk.W)
labelDatos = tk.Label(text='Gary Kasparov')
labelDatos.grid(row=0, column=1, columnspan=2, rowspan=1, sticky=tk.E)
labelProfesion = tk.Label(text='Ajedrecista')
labelProfesion.grid(row=1, column=0, sticky=tk.W)
labelTitulo = tk.Label(text='Campeón Mundial de Ajedrez')
labelTitulo.grid(row=1, column=1, columnspan=2, rowspan=1, sticky=tk.E)
ventana.mainloop()