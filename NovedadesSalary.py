import pandas as pd
import numpy as np
import os

#Leer el Archivo sin cabecera
Salary = pd.read_excel("Base/Novedades.xlsx" , header = None)

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
Salary['Mes de vencimiento'] = str(input('Ingrese el mes de vencimiento en formato MM/AA: '))

#crear carpeta 'Generados' si no existe
if not os.path.exists('Generados'):
    os.makedirs('Generados')


#Exportar las columnas 'Legajo' , 'Concepto 056' , 'Liquidar el concepto' , 'Cantidad 056' , 'Mes de vencimiento' a un archivo llamado '056.txt' cuando el valor de 'Concepto 056' es '056'
Salary[Salary['Concepto 056'] == '056'][['Legajo' , 'Concepto 056' , 'Liquidar el concepto' , 'Nocturnos' , 'Mes de vencimiento']].to_csv('Generados/056.txt' , sep = '|' , index = False , header = False , decimal=",")

#Exportar a las columnas 'Legajo' , 'Concepto 091' , 'Liquidar el concepto' , 'Cantidad 091' , 'Mes de vencimiento' a un archivo llamado '091.txt' cuando el valor de 'Concepto 091' es '091'
Salary[Salary['Concepto 091'] == '091'][['Legajo' , 'Concepto 091' , 'Liquidar el concepto' , 'Feriados' , 'Mes de vencimiento']].to_csv('Generados/091.txt' , sep = '|' , index = False , header = False , decimal=",")

#Exportar a las columnas 'Legajo' , 'Concepto 329' , 'Liquidar el concepto' , 'Cantidad 329' , 'Mes de vencimiento' a un archivo llamado '329.txt' cuando el valor de 'Concepto 329' es '329'
Salary[Salary['Concepto 329'] == '329'][['Legajo' , 'Concepto 329' , 'Liquidar el concepto' , 'L.A.R' , 'Mes de vencimiento']].to_csv('Generados/329.txt' , sep = '|' , index = False , header = False , decimal=",")

#Consolidar todos los .txt de 'Generados' en un solo archivo llamado 'Novedades.txt' 
with open('Generados/Novedades.txt' , 'w') as outfile:
    for fname in os.listdir('Generados'):
        if fname.endswith('.txt'):
            with open(os.path.join('Generados' , fname)) as infile:
                outfile.write(infile.read())

del fname , infile , outfile

#Reemplazando todos los '|' por '' en el archivo 'Novedades.txt'
with open('Generados/Novedades.txt' , 'r') as file:
    filedata = file.read()
filedata = filedata.replace('|' , '')
with open('Generados/Novedades.txt' , 'w') as file:
    file.write(filedata)

del file , filedata