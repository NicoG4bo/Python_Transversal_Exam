import random
import time
import csv
import os
trabajadores = {"Juan Pérez":0,"María García":0,"Carlos López":0, "Ana Martínez":0, "Pedro Rodríguez":0,
                "Laura Hernández":0,"Miguel Sánchez":0, "Isabel Gómez":0, "Francisco Díaz":0, "Elena Fernández":0}
total = 0
total_promedio = 0
promedio_de_sueldos_sum = 0
nombre_sueldo_bajo = " "
nombre_sueldo_alto = " "

def clear():
    os.system('cls')

def continuar():
    os.system('pause')
    os.system('cls')

def sleep():
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print(" ")



def asignar_sueldos ():
    for i,j in trabajadores.items():
        trabajadores[i] = random.randint(300000,2500000)
    clear()
    print("Se han generado los sueldos de los trabajadores aleatoriamente, volviendo al menú principal...")
    sleep()
    clear()
    

def clasificar_sueldos(total):
    print()
    print("A continuación se clasificarán los sueldos\n")
    sueldos_menores = {i:j for i,j in trabajadores.items() if j < 800000}
    count_menores = len(sueldos_menores)
    sueldos_medianos = {i:j for i,j in trabajadores.items() if 800000 <= j <= 2000000}
    count_medianos = len(sueldos_medianos)
    sueldos_grandes = {i:j for i,j in trabajadores.items() if j > 2000000}
    count_grandes = len(sueldos_grandes)
    for i,j in trabajadores.items():
        total += j
    print(f"Sueldos menores a $800.000\nTOTAL: {count_menores}\n")
    print(f"Nombre empleado{' '*18}Sueldo")
    for i,j in sueldos_menores.items():
        print(f"{i:33}${j}")
    print(" ")
    print(f"Sueldos menores entre $800.000 y $2.000.000\nTOTAL: {count_medianos}\n")
    print(f"Nombre empleado{' '*18}Sueldo")
    for i,j in sueldos_medianos.items():
        print(f"{i:33}${j}")
    print(" ")
    print(f"Sueldos superiores a $2.000.000\nTOTAL: {count_grandes}\n")
    print(f"Nombre empleado{' '*18}Sueldo")
    for i,j in sueldos_grandes.items():
        print(f"{i:33}${j}")
    print(" ")
    print(f"TOTAL SUELDOS: ${total}")
    print(" ")

    continuar()

def continuar():
    os.system('pause')
    os.system('cls')

def ver_estadisticas():
    menu_estadisticas()
    
def sueldo_mas_alto():
    maximo = 0
    for i,j in trabajadores.items():
        if maximo < j:
            maximo = j
            nombre_sueldo_alto = i
    print(f"El sueldo más alto es de {nombre_sueldo_alto} con un sueldo de ${maximo}")
    print(" ")
    continuar()
    
def sueldo_mas_bajo():
    minimo = 2500000
    for i,j in trabajadores.items():
        if minimo > j:
            minimo = j
            nombre_sueldo_bajo = i
    print(f"El sueldo más bajo es de {nombre_sueldo_bajo} con un sueldo de ${minimo}")
    print(" ")
    continuar()

def promedio_de_sueldos(total_promedio,promedio_de_sueldos_sum):
    for i,j in trabajadores.items():
        total_promedio += j
    promedio_de_sueldos_sum = total_promedio/10
    print (f" El promedio de los sueldos es de: ${promedio_de_sueldos_sum}")
    print(" ")
    continuar()
    
def media_geometrica():
    print(" ")
    print("Volviendo al menú secundario")
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print(" ")

def salir_menu_estadistica():
    print("Saliendo del MENÚ SECUNDARIO...")
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print(" ")
    return 0


def menu_estadisticas():
    print("Desglosando menú estadísticas en 2 segundos...")
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    sw_menu_estadisticas = 1
    while sw_menu_estadisticas == 1:  
        try:
    
            print("*"*7,"MENU SECUNDARIO","*"*7)
            print("1.- Sueldo más alto")
            print("2.- Sueldo más bajo")
            print("3.- Promedio de sueldos")
            print("4.- Media geométrica")
            print("5.- Salir MENÚ SECUNDARIO")
            print("*"*31)
            op_second = int(input("Ingrese la opción deseada: "))
            print(" ")
            if op_second == 1:
                sueldo_mas_alto()
            elif op_second == 2:
                sueldo_mas_bajo()
            elif op_second == 3:
                promedio_de_sueldos(total_promedio, promedio_de_sueldos_sum)
            elif op_second == 4:
                media_geometrica()
            elif op_second == 5:
                sw_menu_estadisticas = salir_menu_estadistica()
            else:
                print("Ingrese una opción entre 1 y 5, incluyendo estos números")
        except (ValueError,TypeError):
            print("ERROR - Ingresó un carácter inválido")

def reporte_de_sueldos():
    print(f"Nombre empleado{" "*10}Sueldo Base{" "*10}Descuento de Salud{" "*10}Descuento de AFP{" "*10}Sueldo Líquido")
    for i,j in trabajadores.items():
        print(f"{i:25}${j:<20}${round(j*0.07):<27}${round(j*0.12):<25}${round(j*0.81)}")
    print(" ")
    print("Preparando el archivo csv...")
    continuar()
    
    with open('Reporte de sueldos.csv', 'w') as archivo_csv:
        archivo_reporte_csv = csv.writer(archivo_csv)

        archivo_reporte_csv.writerow(["Nombre empleado","Sueldo Base","Descuento de Salud","Descuento de AFP","Sueldo Líquido"])
        for i,j in trabajadores.items():
            nombre = i
            sueldo = j
            desc_salud = round(j*0.07)
            desc_AFP = round(j*0.12)
            sueldo_liquido = round(j*0.81)
            archivo_reporte_csv.writerow([nombre,sueldo,desc_salud,desc_AFP,sueldo_liquido])   
    print("Los datos se han exportado exitósamente en un archivo csv con el nombre de 'Reporte de sueldos.csv'")
    print(" ")
    print("Volviendo al menú principal...")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

def salir():
    print("Finalizando el programa en 3 segundos...")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Desarrollado por Nicolás Lagos\n¡Gracias, Adios!")

    return 0
    
    
def main ():
    sw_main = 1
    while sw_main == 1:
        try: 
            print("*************MENU*************")
            print("1.- Asignar Sueldos aleatorios")
            print("2.- Clasificar Sueldos")
            print("3.- Ver estadísticas")
            print("4.- Reporte de sueldos")
            print("5.- Salir del programa")
            print("******************************")
            op = int(input("Ingrese la opción deseada: "))
            print(" ")
            if op == 1:
                asignar_sueldos() 
            elif op == 2:
                clasificar_sueldos(total)
            elif op == 3:
                ver_estadisticas()
            elif op == 4:
                reporte_de_sueldos()
            elif op == 5:
                sw_main = salir()
        except (ValueError, TypeError):
            print("ERROR - Ingrese un carácter válido")


main()