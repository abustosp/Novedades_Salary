import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
import os
from tkinter import filedialog
from tkinter.messagebox import showinfo

#Obtener el directorio actual 
directorio = os.getcwd()

class DiseñoGuiApp:
    def __init__(self, master=None, translator=None):
        _ = translator
        if translator is None:
            def _(x): return x
        # build ui
        Toplevel_1 = tk.Tk() if master is None else tk.Toplevel(master)
        Toplevel_1.configure(background="#292929", height=230, width=540)
        Toplevel_1.minsize(540, 230)
        Toplevel_1.resizable(False, False)
        Toplevel_1.title("Excel a Salary por Agustín Bustos Piasentini")
        Toplevel_1.iconbitmap("ABP-blanco-en-fondo-negro.ico")
        self.Texto_de_Bienvenida = ttk.Label(Toplevel_1)
        self.Texto_de_Bienvenida.configure(
            anchor="center",
            background="#292929",
            font="{Calibri} 10 {}",
            foreground="#ffffff",
            justify="left",
            state="normal",
            takefocus=False,
            text=_('Generador de Archivos para importar al Salary por ABP'))
        self.Texto_de_Bienvenida.grid(column=1, pady=20, row=0)

        self.Label_Periodo = ttk.Label(Toplevel_1)
        self.Label_Periodo.configure(
            background="#292929",
            font="{calibri} 8 {}",
            foreground="#ffffff",
            justify="center",
            text=_('Inserte el Período en formato MM/AA'))
        self.Label_Periodo.grid(column=1, pady=5, row=2)

        #Crear la variable para el input para el periodo
        Periodo_input = tk.StringVar()

        #Hacer que el boton periodo almacele el valor del input en una variable
        def fun_Periodo():
            Periodo = self.Input_Periodo.get()
            return Periodo
        
        #Seleccionar Archivo y mostrarlo en la consola
        def seleccionarArchivo():
            archivo = filedialog.askopenfilename(initialdir=directorio, title="Selecciona un archivo", filetypes=(("Excel", "*.xls"), ("Excel", "*.xlsx") , ("todos los archivos", "*.*")))
            return archivo

        def procesarArchivo():

            #Obtener las varaibles para generar los arhvivos
            Periodo = fun_Periodo()
            archivo = seleccionarArchivo()
    
            #Leer el Archivo sin cabecera
            Salary = pd.read_excel(archivo , header = None)

            #renombrar las columnas a 'Apellido' , 'Nombre' , 'Legajo' , 'Servicio' , 'Horas' , 'Horas Extra' , 'Nocturnos' , 'Feriados' , 'Susp' , 'Inasist' , 'L.A.R'
            Salary.columns = ['Apellido' , 'Nombre' , 'Legajo' , 'Servicio' , 'Horas' , 'Horas Extra' , 'Nocturnos' , 'Feriados' , 'Susp' , 'Inasist' , 'L.A.R']

            # Filtrar las filas donde 'Legajo' es igual a NaN
            Salary = Salary[Salary['Legajo'].notna()]

            #Rellenar NaN con ceros
            Salary = Salary.fillna(0)

            #Filtrar las que 'Servicio' es igual a NaN
            Salary = Salary[Salary['Servicio'] != 0]

            #Filtrar las que 'Apellido' es igual a NaN
            Salary = Salary[Salary['Apellido'] != 0]

            #Crear columna de 'Concepto 056' con el '056' de 'Nocturnos' si el valor es mayor a cero
            Salary['Concepto 056'] = np.where(Salary['Nocturnos'] > 0, '056' , np.NaN)

            #Crear columna de 'Concepto 091' con el valor de '091' si el valor es mayor a cero
            Salary['Concepto 091'] = np.where(Salary['Feriados'] > 0, '091' , np.NaN)

            #Crear columna de 'Concepto 329' con el valor de '329' si el valor es mayor a cero
            Salary['Concepto 329'] = np.where(Salary['L.A.R'] > 0, '329' , np.NaN)

            #Crear columna de 'Liquidar el concepto' y rellenar con 'S'
            Salary['Liquidar el concepto'] = 'S'

            #Rellenar el 'Legajo' con ceros a la izquierda hasta 3 digitos
            Salary['Legajo'] = Salary['Legajo'].astype(str).str.zfill(3)

            #Mostrar las columnas 'Nocturnos' , 'Feriados', 'L.A.R' con 2 decimales en formato de string mostrando todos los decimales
            Salary['Nocturnos'] = Salary['Nocturnos'].apply(lambda x: '{:.2f}'.format(x))
            Salary['Feriados'] = Salary['Feriados'].apply(lambda x: '{:.2f}'.format(x))
            Salary['L.A.R'] = Salary['L.A.R'].apply(lambda x: '{:.2f}'.format(x))

            #Rellenar las columnas 'Nocturnos' , 'Feriados', 'L.A.R' con 11 ceros (son 14 porque el punto decimal cuenta como un caracter)
            Salary['Nocturnos'] = Salary['Nocturnos'].astype(str).str.zfill(14)
            Salary['Feriados'] = Salary['Feriados'].astype(str).str.zfill(14)
            Salary['L.A.R'] = Salary['L.A.R'].astype(str).str.zfill(14)

            #Crear columnas de 'Mes de vencimiento' y rellenar con el input del usuario
            Salary['Mes de vencimiento'] = Periodo

            #Reemplazar '/' por '-' en la variable 'Periodo'
            Periodo = Periodo.replace('/' , '-')
            
            # Mostrar un messagebox con el mensaje 'Archivo Procesado'
            showinfo("Archivo Procesado", "Archivo Procesado")

            #crear carpeta 'Generados' si no existe
            if not os.path.exists('Generados'):
                os.makedirs('Generados')

            #Crear carpeta 'Generados/Periodo' si no existe
            if not os.path.exists('Generados/' + Periodo):
                os.makedirs('Generados/' + Periodo)

            #Exportar las columnas 'Legajo' , 'Concepto 056' , 'Liquidar el concepto' , 'Cantidad 056' , 'Mes de vencimiento' a un archivo llamado '056.txt' cuando el valor de 'Concepto 056' es '056'
            Salary[Salary['Concepto 056'] == '056'][['Legajo' , 'Concepto 056' , 'Liquidar el concepto' , 'Nocturnos' , 'Mes de vencimiento']].to_csv(f'Generados/{Periodo}/056 - {Periodo}.txt' , sep = '|' , index = False , header = False , decimal=",")

            #Exportar a las columnas 'Legajo' , 'Concepto 091' , 'Liquidar el concepto' , 'Cantidad 091' , 'Mes de vencimiento' a un archivo llamado '091.txt' cuando el valor de 'Concepto 091' es '091'
            Salary[Salary['Concepto 091'] == '091'][['Legajo' , 'Concepto 091' , 'Liquidar el concepto' , 'Feriados' , 'Mes de vencimiento']].to_csv(f'Generados/{Periodo}/091 - {Periodo}.txt' , sep = '|' , index = False , header = False , decimal=",")

            #Exportar a las columnas 'Legajo' , 'Concepto 329' , 'Liquidar el concepto' , 'Cantidad 329' , 'Mes de vencimiento' a un archivo llamado '329.txt' cuando el valor de 'Concepto 329' es '329'
            Salary[Salary['Concepto 329'] == '329'][['Legajo' , 'Concepto 329' , 'Liquidar el concepto' , 'L.A.R' , 'Mes de vencimiento']].to_csv(f'Generados/{Periodo}/329 - {Periodo}.txt' , sep = '|' , index = False , header = False , decimal=",")

            #Consolidar todos los .txt de f'Generados/{Periodo}' en un solo archivo llamado f'Novedades - {Periodo}.txt'
            with open(f'Generados/{Periodo}/Novedades - {Periodo}.txt' , 'w') as outfile:
                for fname in os.listdir(f'Generados/{Periodo}'):
                    if fname.endswith('.txt'):
                        with open(os.path.join(f'Generados/{Periodo}' , fname)) as infile:
                            outfile.write(infile.read())

            del fname , infile , outfile

            #Reemplazando todos los '|' por '' en el archivo 'Novedades.txt'
            with open(f'Generados/{Periodo}/Novedades - {Periodo}.txt' , 'r') as file:
                filedata = file.read()
            filedata = filedata.replace('|' , '')
            with open(f'Generados/{Periodo}/Novedades - {Periodo}.txt' , 'w') as file:
                file.write(filedata)

            del file , filedata
        
        #Entry para ingresar el periodo
        self.Input_Periodo = ttk.Entry(Toplevel_1 , textvariable=Periodo_input)
        self.Input_Periodo.configure(
            cursor="xterm",
            justify="center",
            validate="all",
            width=40)
        self.Input_Periodo.grid(column=1, row=3)

        #botón para seleccionar el archivo y procesarlo
        self.Boton_Procesar = ttk.Button(Toplevel_1)
        self.Boton_Procesar.configure(text=_('Seleccionar, Procesar y Exportar Archivos a la Carpeta "Generados/Periodo"'))
        self.Boton_Procesar.configure(command=procesarArchivo)
        self.Boton_Procesar.grid(column=1, pady=15, row=5)
        
        #una vez que se almacenó el valor del input en la variable Periodo_input, se muestra en el label Periodo_Seleccionado
        self.Periodo_Seleccionado = ttk.Label(Toplevel_1, textvariable=Periodo_input)
        self.Periodo_Seleccionado.configure(
            background="#292929",
            font="{calibri} 8 {}",
            foreground="#999999",
            state="disabled",
            takefocus=False)
        self.Periodo_Seleccionado.grid(column=1, row=4)


        Toplevel_1.grid_propagate(0)
        Toplevel_1.grid_anchor("n")

        # Main widget
        self.mainwindow = Toplevel_1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = DiseñoGuiApp()
    app.run()
