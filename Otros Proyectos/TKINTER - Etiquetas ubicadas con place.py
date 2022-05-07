import tkinter as tk
ventana = tk.Tk()
ventana.geometry('300x100+100+100')
ventana.title('Uso de Etiquetas')
#Creamos Las etiquetas y le damos su ubicación con place
labelUsuario = tk.Label(text='Usuario').place(x=10, y=10)
labelDatos = tk.Label(text='Gary Kasparov').place(x=120, y=10)
labelProfesion = tk.Label(text='Ajedrecista').place(x=10, y=30)
labelTitulo = tk.Label(text='Campeón Mundial de Ajedrez').place(x=120, y=30)
ventana.mainloop()