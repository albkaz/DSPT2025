import math
def area_cuadrado(lado:int|float=0)->int|float:
    """
    Calcula el área de un cuadrado
    
    Input:
        altura: int | float
        base: int | float
        
    Output:
        lado**2: int | float 
    """
    
    return lado**2


def area_triangulo(base: int|float=0, altura: int|float=0)->int|float:
    """
    Calcula el área de un triangulo en base a la altura y la base 
    
    Input:
        altura: int | float
        base: int | float
        
    Output:
        altura * base /2 : int | float 
        
    """
    return altura * base / 2

def area_circulo(radio: int|float=0)->float:
    """
    Calcula el área de un círculo en base al radio
    
    Input:
        base: int | float
    Output:
        Pi * radio ** 2: int | float 
        
    """
    return math.pi * radio**2