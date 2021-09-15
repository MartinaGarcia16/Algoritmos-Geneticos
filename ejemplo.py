import numpy as np
import random

def inicializar():
    filas =10
    columnas=10
    poblacionInicial=50
    #genero array para guardar los 50 genes, cada gen en una matriz de 10x10
    matriz = np.zeros((poblacionInicial,filas,columnas))
    #genero array de indices 
    indices = []
    for i in range(25):
        indices.append([])
        for j in range(2):
            indices[i].append(None)
    return poblacionInicial, indices, filas, columnas, matriz

def verificarIndices():
    ocupado=False
    for f in range(25):
        if indices[f][0]==filaElegida and indices[f][1]==columnaElegida:
            ocupado=True
    return ocupado



poblacionInicial, indices, filas, columnas, matriz = inicializar()

def verificarMolinosJuntos():
    molinosJuntos=False
    if columnaElegida==0:
        if matriz[i][filaElegida][columnaElegida+1]==1:
            molinosJuntos=True
    if columnaElegida==(columnas-1):
        if matriz[i][filaElegida][columnaElegida-1]==1:
            molinosJuntos=True
    if columnaElegida !=0 and columnaElegida !=(columnas-1):
        if matriz[i][filaElegida][columnaElegida+1] ==1 or matriz[i][filaElegida][columnaElegida-1]==1:
            molinosJuntos=True
    return molinosJuntos

for i in range(poblacionInicial):
    ind=0
    for dd in range(25):
        for ff in range(2):
            indices[dd][ff]=None
    cantidadMolinos=random.randint(1,25)
    for x in range(cantidadMolinos):
        aux=0
        while(aux==0):
            filaElegida= random.randint(0,filas-1)
            columnaElegida=random.randint(0,columnas-1)
            
            #comprobar que no esté en el array de indices
            ocupado = verificarIndices()
            #comprobar que no haya dos molinos juntos(teniendo en cuenta que el vento viene de izq a der o viceversa)
            molinosJuntos = verificarMolinosJuntos()
            if ocupado==False and molinosJuntos==False:
                aux=1
                indices[ind][0]=filaElegida
                indices[ind][1]=columnaElegida
                ind=ind+1
                matriz[i][filaElegida][columnaElegida]=1


for x in range(poblacionInicial):
    print('gen nro ', x)
    for z in range(filas):
        print(matriz[x][z])
        print('\n')