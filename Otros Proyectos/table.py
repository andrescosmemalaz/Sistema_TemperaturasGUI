import tkinter as tk
import pandas as pd
from pandastable import Table, TableModel


import tkinter as tk
from pandastable import Table

# root = tk.Tk()

# frame = tk.Frame(root)
# frame.pack()

# pt = Table(frame)
# pt.show()

# root.mainloop()
import tkinter as tk
from pandastable import Table
import pathlib
file = pathlib.Path("Temperatura.xlsx")
df = pd.read_excel(file)


root = tk.Tk()
root.title('PandasTable Example')

frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

pt = Table(frame,dataframe = df)
pt.show()


root.mainloop()







# class DataFrameTable(tk.Frame):
#     def __init__(self, parent=None, df=pd.DataFrame()):
#         super().__init__()
#         self.parent = parent
#         self.pack(fill=tk.BOTH, expand=True)
#         self.table = Table(
#             self, dataframe=df,
#             showtoolbar=False,
#             showstatusbar=True,
#             editable=False)
#         self.table.show()


# df = pd.DataFrame({"Foo": (1, 2, 3, 4,5), "Bar": (7, 13, 17, 19,25)})
# root = tk.Tk()
# table = DataFrameTable(root, df)
# root.mainloop()

# # df = pd.DataFrame({'numeros':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]})

# # table  = tk.Tk()
# # table.title('Tabla simple')

# # frame = tk.Frame(table)
# # frame.pack()

# # pt = Table(frame,dataframe=df,showtoolbar=True,showstatusbar=True)
# # pt.show()

# table.mainloop()


