"""
Doc-string
"""

import numpy as np
import pandas as pd


# def matriz_cuadrada_alterna(orden:int)->np.ndarray:
#     """ 
#     Dado un orden, devuelve una matriz cuadrada con los valores alternos 0-1
#     Ejemplo de resultado con orden=4
#     [
#         [0, 1, 0, 1],
#         [1, 0, 1, 0],
#         [0, 1, 0, 1],
#         [1, 0, 1, 0]
#     ]
    
#     Inputs:
#         orden: int orden de la matriz cuadrada
        
#     Outputs:
#         matriz: ndarray
#     """
#     # Voy a sacar el 1 ó 0 a partir del modulo dividiendo la posición entre 2 (par vs impar)
#     # Daré un valor a cada celda que será la posicion secuencial en la matriz orden x orden
#     # Es una secuencia del 0 al orden^2-1, que será la posicion secuencial para todos los elementos
#     secuencia_inicial = np.arange(orden**2).reshape(orden,orden)
#     print(f"Posiciones secuenciales en la matriz {orden}x{orden}\n", secuencia_inicial, "\n")

#     # En función del número de columnas, el inicio de las filas impares tiene que ser un valor par o impar.
#     # Voy a crear una matriz de 2 dimensiones 1 x orden que tendrá 0 o 1.
#     # En las filas pares tenrá el valor 0 y en los impares 1 si el orden es par y 0 si el orden es impar
#     vector_orden = np.zeros(orden, dtype=np.int8) # vector de "orden" con valores a 0
#     vector_orden[1::2] = (orden+1) % 2 # modicamos los valores en las posiciones impares para que valga 1 si el orden es par.
#     matriz_orden = vector_orden.reshape(-1,1) # creamos una matriz de 1 x orden a partur del vector anterior
    
#     print(F"Matriz 1x{orden}\n", matriz_orden, "\n")
    
    
#     # Sumo la nueva matriz a la matriz secuencia_inicial y así se modificarán los elementos por fila,
#     # sumando el único valor de la fila de la matriz matriz_orden a cada uno de los elementos de la fila de la matriz secuencia_inicial
#     matriz_secuencia_alterna = secuencia_inicial + matriz_orden

#     # ahora ya tengo una matriz donde hay "orden" filas y "orden" columnas
#     # donde los valores de las columnas en cada fila son consecutivos (al dividir entre 2 el modulo me dará 1 ó 0)
#     # y el número inicial de la columna por cada fila es par/impar consecutivamente.    
#     print(F"Resultado suma de las matrices\n", matriz_secuencia_alterna, "\n")
    
#     # saco el modulo de la division entre 2 para toda la matriz
#     return matriz_secuencia_alterna % 2


# print("Matriz cuadrada alterna:\n", matriz_cuadrada_alterna(6))


a = """
El proyecto consiste en ver las materias impartidas a través de un proyecto que tenga un impacto en el mundo real. Para ello, los alumnos tuvieron que reunirse y proponer distintos problemas reales de la ciudad en la que vivían, para después debatir cuales eran viables y cuales no, y entre la viables seleccionar una de ellas. Se seleccionó digitalizar un producto con impacto directo en el turismo: “Ávila en tapas”, el evento gastronómico más importante de la ciudad.
Metodología
El desarrollo del proyecto se realizó con trabajo en equipo, en un único grupo de 10 alumnos para resolver el mismo problema.  El grupo se dividió en 3 subgrupos distintos que debían coger los roles de los 3 actores principales implicados del proyecto: organizador del evento, usuarios y restaurantes. Cada cierto tiempo se intercambiaban los roles de los alumnos de forma que tuvieran la visión de los 3 subgrupos.
Estos subgrupos aportaban necesidades, ideas y soluciones en función del rol asumido.
A partir de este punto, partiendo de las metodologías Ágiles (meter cita) Scrum, Kanban y Extreme Programming, aunque adaptándolas a la situación del aula, 
"""
print(len(a.split(" ")))