from random import randint
n=0
cantidad_pi=10
cantidad_genes=30
cromosomas_binario=[]
cromosomas_decimal=[]
lista_funcion_obj=[]
fitness=[]


def crearPoblacionBinario():
 for x in range(cantidad_pi):
    cromosomas_binario.append([])
    for j in range(cantidad_genes):
        n=randint(0,1)
        cromosomas_binario[x].append(n) 

def crearLista(a,lista):
    for x in range(a):
        lista.append(None)

def convertirDecimal():
    for x in range(cantidad_pi):
        suma=0
        for j in range(cantidad_genes):
            if cromosomas_binario[x][j]==1:
                suma+=(2**(cantidad_genes-(j+1)))
        cromosomas_decimal[x]=suma

def funcionObjetivo(a):
  return  (a/((2**30)-1))**2

def calculaSPM():
    suma=0
    maxi=lista_funcion_obj[0]
    mini=lista_funcion_obj[0]
    for x in range(cantidad_pi):
        suma+=lista_funcion_obj[x]
        if (lista_funcion_obj[x]>= maxi):
            maxi=lista_funcion_obj[x]
        if (lista_funcion_obj[x]<= mini):
            mini=lista_funcion_obj[x]
    lista_funcion_obj[cantidad_pi]=suma
    lista_funcion_obj[cantidad_pi+1]=maxi
    lista_funcion_obj[cantidad_pi+2]= (suma/cantidad_pi)
    lista_funcion_obj[cantidad_pi+3]= mini

#calculo el fitness de cada cromosoma 
def calcular_fitness(suma,maxi,mini):
    for i in range(10):
        x= (lista_funcion_obj[i]/suma)
        fitness[i] = x

#main
#creando y cargando la matriz de cromosomas (poblacion inicial)
crearPoblacionBinario()
#mostrando las matriz binaria
print("POBLACION INICIAL BINARIA")
for x in range(10):
    for j in range(30):
        print(cromosomas_binario[x][j],end=" ")
    print()
#creando lista decimal
crearLista(cantidad_pi, cromosomas_decimal)
#creo lista de fitness
crearLista(cantidad_pi,fitness)
#convirtiendo a decimal
convertirDecimal()
#mostrando decimal 
print("\nPOBLACION INICIAL EL DECIMALES")  
for x in range(10):
    print(cromosomas_decimal[x])
#crear valores funcion objetivo (le agrego 3 lugares mas para guardar max, suma y promedio)
crearLista((cantidad_pi+4),lista_funcion_obj)
#valores funcion objetivo
for x in range(cantidad_pi):
    lista_funcion_obj[x]= funcionObjetivo(cromosomas_decimal[x])

#calcular suma promedio maximo
calculaSPM()
suma= lista_funcion_obj[10]
maxi= lista_funcion_obj[11]
prom = lista_funcion_obj[12]
mini= lista_funcion_obj[13]
#calcular fitness
calcular_fitness(suma,maxi,prom)
#mostrar funcion objetivo
print('\nFUNCION OBJETIVO')
for i in range (10):
    print(lista_funcion_obj[i])
'''for x in range(13):
    if x==10:
        print("suma")
    if x==11:
        print("maximo")
    if x==12:
        print("promedio")
    print(lista_funcion_obj[x])'''
print('\nSUMA:', end=" ") 
print(suma)
print('MAXIMO:', end=" ") 
print(maxi)
print('MINIMO:', end=" ") 
print(mini)
print('PROMEDIO:', end=" ") 
print(prom)

print('\nFITNESS')
for i in range (len(fitness)):
    print(fitness[i])
sumafitnees=0
for i in range (len(fitness)):
    sumafitnees+=fitness[i]
print (sumafitnees)
"""import random
import collections
import statistics
import numpy

coef = (2 ** 30) - 1
ciclos = 1
pc = 0.75
pm = 0.05
cromosomas = []
decimales = []
fitness = []


# cant_individuos=10

def crear_pob_inicial(cant_individuos):
    for i in range(0, cant_individuos):
        binario = numpy.random.randint(2, size=30)
        cromosomas.append(binario)


def convertir_decimal():
    for i in range(0, 10):
        suma = 0
        for j in range(0, 30):
            if (cromosomas[i] == 1):
                suma = suma + pow(2, coef - j)
        decimales.append(suma)
    print(cromosomas)


def funcion_obj(x):
    return (x / (2 ** 30) - 1)


crear_pob_inicial(10)
for i in range(0, ciclos):
    convertir_decimal()
    minimo = min(decimales)
    maximo = max(decimales)
    prom = statistics.mean(decimales)
    for j in range(0, 10):
        suma_fo = sum(funcion_obj(decimales[j]))
    for k in range(0, 10):
        fitness.append(decimales[k] / suma_fo)
        suma_fitness = sum(fitness[k])
    prom_fitness = statistics.mean(fitness)
    maximo_fitness = max(fitness)
    minimo_fitness = min(fitness)
print(decimales)
print(fitness)

sacar maximo
maximo=-1
    for arg in args:
        if arg > maximo:
            maximo = arg
    return maximo 
def maximo_arbitrario(*args) -> float:"""
