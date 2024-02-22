import customtkinter as ctk
import os


import tkinter as tk
from tkinter import filedialog

# Crear la ventana principal
ventana = ctk.CTk()
ventana.title("Ventana con Customtkinter")
ventana.geometry("400x400")  # Ancho x Alto

 
# Funciones para los botones 
def seleccionarArchivo():
    archivo = filedialog.askopenfilename(initialdir="/", title="Selecciona un archivo", filetypes=(("archivos de texto", "*.txt"), ("todos los archivos", "*.*")))

    if archivo != '':
        print(archivo)

    
def procesarArchivo():  # Aqui va el codigo para procesar el archivo seleccionado

    print("Archivo Procesado")

    
def exportarArchivo():  # Aqui va el codigo para exportar el archivo procesado

    print("Archivo Exportado")

    
# Creando los botones y labels de la ventana principal 
label = ctk.CTkLabel(ventana, text="Generador de TXT de novedades del Salary")  # Label de la ventana principal  
label.pack()   # Empaquetamos el label en la ventana principal  

def button_click_event():
    dialog = ctk.CTkInputDialog(text="Escribir el Período en formato MM/AA", title="Período")
    Input = dialog.get_input()
    return Input

def printValue():
    Per = Periodo.get()
    ctk.CTkLabel(ventana, text=f'El período ingresado es {Per}' ).pack(pady=20)


Periodo = ctk.CTkEntry(ventana)
Periodo.pack(pady=30)

ctk.CTkButton(
    ventana,
    text="Ingrese el Período",
    command=printValue
    ).pack(pady=5)

# Boton para abrir un dialogo y obtener el input en una variable
botonDialogo = ctk.CTkButton(ventana, text="Abrir Dialogo", command=button_click_event)
botonDialogo.pack(pady=5)


  # Boton para seleccionar un archivo  
botonSeleccionar = ctk.CTkButton(ventana, text="Seleccionar Archivo", command=seleccionarArchivo)   # Creamos el boton con su respectiva funcion  
botonSeleccionar.pack(pady=5)   # Empaquetamos el boton en la ventana principal  

  # Boton para procesar un archivo  
botonProcesar = ctk.CTkButton(ventana, text="Procesar Archivo", command=procesarArchivo)   # Creamos el boton con su respectiva funcion  
botonProcesar.pack(pady=5)   # Empaquetamos el boton en la ventana principal  

  # Boton para exporta un archivo   												   
botonExporta = ctk.CTkButton(ventana, text="Exporta Archivos", command=exportarArchivo)    # Creamos el boton con su respectiva funcion
botonExporta.pack(pady=5)    # Empaquetamos el botón en la ventana principal      




# if dialog is not None:      
#     print(inputDialog)   
# else:
#     print('No ingresaste nada')      

  # Bucle de ejecución de la ventana principal
ventana.mainloop()