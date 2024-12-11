import random 
from tabulate import tabulate
from termcolor import colored
import os


#configuracion
intentos = 100000
prisioneros = 100

aperturas = prisioneros//2 


def Sin_estrategia(lista, numero):

    caja_random = random.sample(range(prisioneros), aperturas)
    for i in range(aperturas):
        if lista[caja_random[i]] == numero:
            return True
        
    return False
    

def ciclica(lista, numero):

    lugar = numero
    for i in range(aperturas):
        if lista[lugar] != numero:
            lugar = lista[lugar]
        else:
            return True
    return False
        

        
def pricioneros(funcion, lista):

    for i in range(prisioneros):
        encontrar = funcion(lista, i)
        if encontrar == False:
            return False
    
    return True


def estadistica(funcion):
    sobreviven = 0
    mueren = 0
    
    for i in range(intentos):
        lista = list(range(prisioneros))
        random.shuffle(lista)

        vivieron = pricioneros(funcion, lista)
        if vivieron == True:
            sobreviven = sobreviven + 1
        else:
            mueren = mueren + 1
        
    porcentaje_de_supervivencia = (sobreviven/(sobreviven + mueren)) * 100
    return sobreviven, mueren, porcentaje_de_supervivencia



def imprimir_estadisticas(nombre_estrategia, sobreviven, mueren, porcentaje_de_supervivencia):
    table = [
        ["Estadísticas para la estrategia", colored(nombre_estrategia, "green")],
        ["Se intentaron", sobreviven + mueren],
        [colored("Sobrevivieron", "green"), sobreviven],
        [colored("Murieron", "red"), mueren],
        ["Porcentaje de supervivencia", f"{porcentaje_de_supervivencia:.2f}%"]]
    
    print(tabulate(table, tablefmt="fancy_grid"))

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


instrucion = " "


while instrucion != "3":
    print(instrucion)
    instrucion = " "

    while instrucion != "" and instrucion != "3":
        limpiar_consola()
        print(colored("\t\t\t┌─────────────────────────────────────────────┐", "cyan"))
        print(colored("\t\t\t│      Simulador del puzzle prisioneros       │", "cyan"))
        print(colored("\t\t\t└─────────────────────────────────────────────┘", "cyan"))
        print()

        opciones = [
            ["1", "Cambiar la cantidad de prisioneros", "Actualmente configurado en " + str(prisioneros) + " prisioneros."],
            ["2", "Cambiar la cantidad de intentos", "Actualmente configurado en " + str(intentos) + " inte1ntos."],
            ["3", "Finalizar el programa", "Recomiendo colocar un numero par en la cantidad"],
            ["", "Si no desea realizar más modificaciones, solo presione Enter", "de prisioneros"]
        ]
        print(tabulate(opciones, headers=["Opción", "Descripción", ""]), end="\n\n")

        instrucion = input(colored("Ingrese su opción: ", "yellow"))

        if instrucion == "1":
            valor = input("ingrese la nueva cantidad de prisioneros: ")    
            while not(valor.isdigit()) or valor == "0": 
                valor = input(colored("Ese valor no es valido, porfavor solo introdusca numeros Naturales: ", "red"))

            prisioneros = int(valor)
            aperturas = prisioneros//2 

        elif instrucion == "2":
            valor = input("ingrese la nueva cantidad de intentos: ")    

            while not(valor.isdigit()) or valor == "0": 
                valor = input(colored("Ese valor no es valido, porfavor solo introdusca numeros Naturales: ", "red"))

            intentos = int(valor)

        elif instrucion == "3":
            continue
       
    if instrucion == "3":
        continue
    limpiar_consola()
    print(colored("Calculando estadisticas, por favor espere...\n", "green"))
    sobreviven_ciclica, mueren_ciclica, porcentaje_ciclica = estadistica(ciclica)
    imprimir_estadisticas("ciclica", sobreviven_ciclica, mueren_ciclica, porcentaje_ciclica)

    sobreviven_sin_estrategia, mueren_sin_estrategia, porcentaje_sin_estrategia = estadistica(Sin_estrategia)
    imprimir_estadisticas("sin estrategia", sobreviven_sin_estrategia, mueren_sin_estrategia, porcentaje_sin_estrategia)
    input(colored("Precione enter para volver al menu \n", "yellow"))
    limpiar_consola()
