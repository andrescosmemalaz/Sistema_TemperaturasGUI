import tkinter as tk
def convierte():
    temp = int(entrada.get())
    temp = 9/5*temp+32
    etiquetaSalida.configure(text = 'En Fahrenheit: {:.1f}'.format(temp))
    entrada.delete(0,tk.END)

raiz = tk.Tk()
raiz.geometry('400x100')
raiz.title("Convertir de Celsius a Fahrenheit")

etiquetaMsg = tk.Label(text='Ingrese temperatura °C', font=('Calibri', 14))
etiquetaMsg.grid(row=0, column=0)

etiquetaSalida = tk.Label(font=('Calibri', 14))
etiquetaSalida.grid(row=1, column=0, columnspan=3)

entrada = tk.Entry(font=('Calibri', 14), width=4)
entrada.grid(row=0, column=1)

botonCalc = tk.Button(text='Convertir', font=('Calibri', 14), command=convierte)
botonCalc.grid(row=0, column=2)

raiz.mainloop()
