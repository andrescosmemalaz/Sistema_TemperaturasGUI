import tkinter as tk
ventana = tk.Tk()
ventana.geometry('300x100+100+100')
ventana.title('Uso de Etiquetas')
#Creamos Las etiquetas
labelUsuario = tk.Label(text='Usuario')
labelDatos = tk.Label(text='Gary Kasparov')
labelProfesion = tk.Label(text='Ajedrecista')
labelTitulo = tk.Label(text='Campeón Mundial de Ajedrez')
#Agregamos la eiqueta a la ventana
labelUsuario.pack(side='left')
labelDatos.pack(side='right')
labelProfesion.pack(side='top')
labelTitulo.pack(side='bottom')
ventana.mainloop()
