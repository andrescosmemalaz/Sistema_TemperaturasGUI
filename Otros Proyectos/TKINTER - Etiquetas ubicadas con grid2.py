import tkinter as tk
ventana = tk.Tk()
ventana.geometry('300x100+100+100')
ventana.title('Uso de Etiquetas')
#Creamos Las etiquetas y le damos su ubicación con grid
labelUsuario = tk.Label(text='Usuario').grid(row=0, column=0, sticky=tk.W)
labelDatos = tk.Label(text='Gary Kasparov').grid(row=0, column=1, sticky=tk.W)
labelProfesion = tk.Label(text='Ajedrecista').grid(row=1, column=0,
sticky=tk.E)
labelTitulo = tk.Label(text='Campeón Mundial de Ajedrez').grid(row=1, column=1,
sticky=tk.E)
ventana.mainloop()
