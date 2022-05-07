import tkinter as tk
ventana = tk.Tk()
ventana.geometry('400x400+100+100')
ventana.title('Uso de Etiquetas')
#Creamos Las etiquetas
labelUsuario = tk.Label(text='Nombre')
labelDatos = tk.Label(text='Andres')
labelUsuario_2 = tk.Label(text='Apellido Paterno')
labelDatos_2 = tk.Label(text='Cosme')
labelUsuario_3 = tk.Label(text='Apellido Materno')
labelDatos_3 = tk.Label(text='Malasquez')
#Agregamos las etiquetas a la ventana
labelUsuario.pack()
labelDatos.pack()
labelUsuario_2.pack()
labelDatos_2.pack()
labelUsuario_3.pack()
labelDatos_3.pack()
ventana.mainloop()
