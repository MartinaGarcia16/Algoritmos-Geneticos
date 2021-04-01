import random
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

"""sacar maximo
maximo=-1
    for arg in args:
        if arg > maximo:
            maximo = arg
    return maximo 
def maximo_arbitrario(*args) -> float:"""
