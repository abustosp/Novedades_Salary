import pandas as pd
import numpy as np

#Leer excel "Planilla de Sueldos Oberá.xlsx" a aprtir de la octava fila con los encabezados en la setima fila
Novedades = pd.read_excel('Base/Planilla de Sueldos Oberá.xlsx' , skiprows=6 , header=0)

Novedades = Novedades.fillna(0)

#Filtrar los legajos que no estan en blanco
Novedades = Novedades[Novedades['Leg'] != 0]

#reemplarar en la columna 'Asist. - C-8' los 'NO' por '0'
Novedades['Asist. - C-8'] = Novedades['Asist. - C-8'].replace('NO', 0)

#Reemplazar en la columna 'Observaciones' los '0' por np.nan
Novedades['Observaciones'] = Novedades['Observaciones'].replace(0, np.nan)

#mostrar los datos de las columnas 'Horas Simple C-3' , 'Horas Extras al 50 % C-4' , 'Sábados Posterior a las 13:00 Hs. C-5' , 'Dom. Todo el Dia C-5' , 'Cond. C-41' , 'Tareas Varias - C-42' , 'Reposo - C-10' , 'Dias ART - C-15 y C-14' , 'Lic. Reg. - C-16' , 'Asig No Rem C-325' , 'Bono Reg 230/22 a Cta. C-347' , 'Asist. - C-8' con 2 decimales en formato de string mostrando todos los decimales
Novedades[['Horas Simple C-3' , 'Horas Extras al 50 % C-4' , 'Sábados Posterior a las 13:00 Hs. C-5' , 'Dom. Todo el Dia C-5' , 'Cond. C-41' , 'Tareas Varias - C-42' , 'Reposo - C-10' , 'Dias ART - C-15 y C-14' , 'Lic. Reg. - C-16' , 'Asig No Rem C-325' , 'Bono Reg 230/22 a Cta. C-347' , 'Asist. - C-8']] = Novedades[['Horas Simple C-3' , 'Horas Extras al 50 % C-4' , 'Sábados Posterior a las 13:00 Hs. C-5' , 'Dom. Todo el Dia C-5' , 'Cond. C-41' , 'Tareas Varias - C-42' , 'Reposo - C-10' , 'Dias ART - C-15 y C-14' , 'Lic. Reg. - C-16' , 'Asig No Rem C-325' , 'Bono Reg 230/22 a Cta. C-347' , 'Asist. - C-8']].applymap(lambda x: '{:.2f}'.format(x))

#Rellenzar con ceros a la izquierda hasta llegar a los 10 caracteres de las columnas 'Horas Simple C-3' , 'Horas Extras al 50 % C-4' , 'Sábados Posterior a las 13:00 Hs. C-5' , 'Dom. Todo el Dia C-5' , 'Cond. C-41' , 'Tareas Varias - C-42' , 'Reposo - C-10' , 'Dias ART - C-15 y C-14' , 'Lic. Reg. - C-16' , 'Asig No Rem C-325' , 'Bono Reg 230/22 a Cta. C-347' , 'Asist. - C-8'
Novedades[['Horas Simple C-3' , 'Horas Extras al 50 % C-4' , 'Sábados Posterior a las 13:00 Hs. C-5' , 'Dom. Todo el Dia C-5' , 'Cond. C-41' , 'Tareas Varias - C-42' , 'Reposo - C-10' , 'Dias ART - C-15 y C-14' , 'Lic. Reg. - C-16' , 'Asig No Rem C-325' , 'Bono Reg 230/22 a Cta. C-347' , 'Asist. - C-8']] = Novedades[['Horas Simple C-3' , 'Horas Extras al 50 % C-4' , 'Sábados Posterior a las 13:00 Hs. C-5' , 'Dom. Todo el Dia C-5' , 'Cond. C-41' , 'Tareas Varias - C-42' , 'Reposo - C-10' , 'Dias ART - C-15 y C-14' , 'Lic. Reg. - C-16' , 'Asig No Rem C-325' , 'Bono Reg 230/22 a Cta. C-347' , 'Asist. - C-8']].applymap(lambda x: x.zfill(10))
