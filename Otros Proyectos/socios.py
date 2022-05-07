import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Label, Button,Entry, Frame, END, font
import pandas as pd 
import openpyxl
from tkinter import messagebox

ventana = Tk()
ventana.config(bg='yellow')
ventana.geometry('610x470')
ventana.resizable(0,0)
ventana.title('CRUD de Socios del Club')

nombre_socio = []
apellido_paterno_socio = []
apellido_materno_socio = []
codigo_socio = []
fecha_ingreso= []
cuota_dia = []
monto = []

# def funcion_click():
#     respuesta = ttk.Label(ventana,text="Seleccionado " + opcion.get())
#     respuesta.grid(column=1, row=3)

def ingreso_datos():
    x = ingresa_codigo_socio.get()
    if x in codigo_socio:
        tk.messagebox.showwarning(title="Alerta", message="El código ya existe en la base de datos",detail="Ingresé otro código")
        ingresa_nombre_socio.delete(0,tk.END)
        ingresa_apellido_paterno_socio.delete(0,tk.END)
        ingresa_apellido_materno_socio.delete(0,tk.END)
        ingresa_codigo_socio.delete(0,tk.END)
        ingresa_fecha_ingreso.delete(0,tk.END)
        ingresa_monto.delete(0,tk.END)

    else:
        nombre_socio.append(ingresa_nombre_socio.get())
        apellido_paterno_socio.append(ingresa_apellido_paterno_socio.get())
        apellido_materno_socio.append(ingresa_apellido_materno_socio.get())
        codigo_socio.append(ingresa_codigo_socio.get())
        cuota_dia.append(opcion.get())
        fecha_ingreso.append(ingresa_fecha_ingreso.get())
        monto.append(ingresa_monto.get())

        ingresa_nombre_socio.delete(0,tk.END)
        ingresa_apellido_paterno_socio.delete(0,tk.END)
        ingresa_apellido_materno_socio.delete(0,tk.END)
        ingresa_monto.delete(0,tk.END)
        ingresa_codigo_socio.delete(0,tk.END)
        ingresa_fecha_ingreso.delete(0,tk.END)

def guardar_datos():
    data = {'Nombres': nombre_socio, 'Apellido Paterno':apellido_paterno_socio ,'Apellido Materno': apellido_materno_socio,'Codigo':codigo_socio, 'Fecha de Ingreso':fecha_ingreso, '¿Pago cuota?':cuota_dia, 'Monto':monto}
    nombre_excel = str(nombre_archivo.get()+'.xlsx')
    df = pd.DataFrame(data, columns=['Nombres','Apellido Paterno','Apellido Materno','Codigo','Fecha de Ingreso','¿Pago cuota?','Monto'])
    df.to_excel(nombre_excel)
    nombre_archivo.delete(0,tk.END)


frame1 = Frame(ventana, bg='yellow')
frame1.grid(column=0, row=0, sticky='nsew')
fram2 = Frame(ventana, bg='yellow')
fram2.grid(column=1, row=0, sticky='nsew')


nombre = Label(frame1, text ='Nombre', width=10).grid(column=0, row=0, pady=20, padx= 10)
ingresa_nombre_socio = Entry(frame1,  width=20, font = ('Arial',12))
ingresa_nombre_socio.grid(column=1, row=0)

apellido_paterno = Label(frame1, text='A. paterno', width=10).grid(column=0, row=1, pady=20, padx=10)
ingresa_apellido_paterno_socio = Entry(frame1, width= 20, font = ('Arial',12))
ingresa_apellido_paterno_socio.grid(column=1, row=1)

apellido_materno = Label(frame1, text='A. materno', width=10).grid(column=0, row=2, pady=20, padx=10)
ingresa_apellido_materno_socio = Entry(frame1, width=20, font=('Arial',12))
ingresa_apellido_materno_socio.grid(column=1, row=2)

codigo =Label(frame1,text='Codigo', width=10).grid(column=0, row=3, pady=20, padx=10)
ingresa_codigo_socio = Entry(frame1, width=20, font= ('Arial',12))
ingresa_codigo_socio.grid(column=1, row=3)

fecha = Label(frame1, text='F. nacimiento', width=10).grid(column=0, row=4, pady=20, padx=10)
ingresa_fecha_ingreso = Entry(frame1, width=20, font=('Arial',12))
ingresa_fecha_ingreso.grid(column=1, row=4)


etiqueta = ttk.Label(frame1, text='Cumple Cuota')
etiqueta.grid(column=0,row=5)
opcion = tk.StringVar()
seleccionar_opcion = ttk.Combobox(frame1, width=27, textvariable=opcion,state='readonly')
seleccionar_opcion['values'] = ('SI','NO')
seleccionar_opcion.grid(column=1,row=5)
seleccionar_opcion.current(0)

dinero = Label(frame1, text= 'Monto pago',width=10).grid(column=0,row=7, pady=20,padx=10)
ingresa_monto = Entry(frame1, width=20, font=('Arial',12))
ingresa_monto.grid(column=1, row=7)

agregar = Button(frame1,width=20, font=('Arial',12,'bold'), fg='white', text='Registrar', bg='blue', bd=5, command=ingreso_datos)
agregar.grid(column= 1, row=8, pady=20, padx=10)

archivo = Label(fram2, text='Nombre del archivo', width=25, bg='gray16', font=('Arial',12,'bold'), fg='white')
archivo.grid(column=0, row=0,pady=10,padx=10)

nombre_archivo = Entry(fram2, width=23, font=('Arial',12), highlightbackground='red',highlightthickness=4)
nombre_archivo.grid(column=0,row=1, pady=1, padx= 10)

guardar = Button(fram2, width=20, font=('Arial',12,'bold'), text='Guardar', bg='green1', bd=5, command=guardar_datos)
guardar.grid(column=0, row=2, pady=20,padx=10)

ventana.mainloop()