from random import randint
from random import random

n=0
cantidad_pi=10
cantidad_genes=30
cantidad_ciclos=20
cromosomas_binario=[]
cromosomas_decimal=[]
lista_funcion_obj=[]
lista_porcentajes=[]
fitness=[]
prob_cross=0.75
prob_mut=0.05
padres=[]
probabilidades=[]
cromosomas_hijo=[]
punto_corte = 1
hijos=[] #tiene la nueva poblacion, con crossover o con mutación
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
            nro_max=cromosomas_decimal[x] #el nro decimal que me genera el valor de f. objt. mas grande lo guardo en nro_max
        if (lista_funcion_obj[x]<= mini):
            mini=lista_funcion_obj[x]
    lista_funcion_obj[cantidad_pi]=suma
    lista_funcion_obj[cantidad_pi+1]=maxi
    lista_funcion_obj[cantidad_pi+2]=nro_max
    lista_funcion_obj[cantidad_pi+3]= (suma/cantidad_pi)
    lista_funcion_obj[cantidad_pi+4]= mini

#calculo el fitness de cada cromosoma 
def calcular_fitness(suma,maxi,mini):
    for i in range(10):
        x= (lista_funcion_obj[i]/suma)
        fitness[i] = x

def porcentajes(lista_porcentajes):
    acum=0
    for i in range(10):
        porc= fitness[i]*100
        for j in range(round(porc)):
            lista_porcentajes[acum] = i
            acum+=1
            if(acum==100):
                break
    return acum

def seleccionar_padres(acum,padres):
    for i in range(cantidad_pi):
        x= randint(0,acum)
        padres[i]=lista_porcentajes[x]

def hacer_crossover():
    #crearLista(cantidad_genes,cromosomas_hijo)
    padre1=[]
    padre2=[]
    for i in range (0,int(len(cromosomas_decimal)/2)):
        x= randint(0,acum)
        cromosoma_nuevo_1=cromosomas_binario[lista_porcentajes[x]]
        y=randint(0,acum)
        cromosoma_nuevo_2=cromosomas_binario[lista_porcentajes[y]]
        print('padre1')
        print(cromosoma_nuevo_1)
        print('padre2')
        print(cromosoma_nuevo_2)
        
        if (random() <= prob_cross): 
            aux=[]
            crearLista(30,aux)            
            for x in range (0,len(padre2)):
                aux[x] = cromosoma_nuevo_2[x]
            for x in range (punto_corte,len(padre2)):  #crossover desde el punto corte hasta fin
                cromosoma_nuevo_2[x] = cromosoma_nuevo_1[x]
                cromosoma_nuevo_1[x] = aux[x]
            print('hijo1')
            print(cromosoma_nuevo_1)
            print('hijo2')
            print(cromosoma_nuevo_2)
            
        if (random() <= prob_mut):
            x=randint(0,29)
            valor1=cromosoma_nuevo_1[x] #busco el valor 1 o 0 en esa posicion
            if (valor1==1):
                cromosoma_nuevo_1[x]==0
            else:
                cromosoma_nuevo_1[x]==1

        if (random() <= prob_mut):
            y=randint(0,29)
            valor2=cromosoma_nuevo_2[y]
            if(valor2==1):
                cromosoma_nuevo_2[y]==0
            else:
                cromosoma_nuevo_2==1

        hijos.append(cromosoma_nuevo_1)
        hijos.append(cromosoma_nuevo_2)              


#MAIN
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
crearLista((cantidad_pi+5),lista_funcion_obj)
#valores funcion objetivo
for x in range(cantidad_pi):
    lista_funcion_obj[x]= funcionObjetivo(cromosomas_decimal[x])

#calcular suma promedio maximo minimo 
nro_max=0
calculaSPM()
suma= lista_funcion_obj[10]
maxi= lista_funcion_obj[11]
nro_max= lista_funcion_obj[12]
prom = lista_funcion_obj[13]
mini= lista_funcion_obj[14]

#calcular fitness

calcular_fitness(suma,maxi,prom)
crearLista(100,lista_porcentajes)
acum= porcentajes(lista_porcentajes)
#crearLista(cantidad_pi,padres)
#seleccionar_padres(acum,padres)
#crearLista(100, probabilidades)
hacer_crossover()
'''for i in range(5):
    for k in range(75):
        probabilidades[k]= 1
        for j in range(25):
            probabilidades[j+75]=0
        x=randint(0,100)
        if (probabilidades[x]==1):
            hacer_crossover(probabilidades, padres, i)'''
        
#mostrar funcion objetivo
print('\nFUNCION OBJETIVO')
for i in range (10):
    print(lista_funcion_obj[i])

print('\nSUMA:', end=" ") 
print(suma)
print('MAXIMO:', end=" ") 
print(maxi)
print('Cromosoma que genera el valor máximo:', end=" ") 
print(nro_max)
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

print('\nPOOL GENERADO:')
print(lista_porcentajes)
#print(len(lista_porcentajes))
print('ACUMULADOR DEL POOL: ', end=" ")
print(acum)
#print(padres)
#print(probabilidades)
print('\nPOBLACION HIJOS')
for i in range (len(hijos)):
    print(hijos[i])






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