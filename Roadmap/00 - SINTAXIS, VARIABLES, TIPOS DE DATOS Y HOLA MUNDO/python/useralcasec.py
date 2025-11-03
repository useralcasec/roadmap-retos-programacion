# https://www.python.org/

# Comentario de una linea

"""
Este es un comentario
de múltiples líneas
"""

'''
Este es otro comentario
de múltiples líneas
'''

"""
Nombres de variables en Python
Según la PEP 8 los nombres de las variables de Python deben de escribirse en snake_case. Además se deben de cumplir las siguientes características:

Tienen que empezar por una letra o barra baja.
El uso de keywords como nombres está prohibido.
Los nombres deben de ser descriptivos.
Deben de estar en minúsculas y separando palabras por barras bajas ‘_’.
Las constantes se escriben en mayúsculas y SNAKE_CASE.

Fuente: https://elpythonista.com/variables-python
"""

my_variable = "Esto es una variable"
MY_CONSTANT = "Esto es una constante"

# TIPOS DE DATOS PRIMITIVOS
# Entero (int)
"""
Representa números enteros, positivos o negativos, sin parte fraccionaria.
"""
entero = 10
print(entero)
print(type(entero)) # Imprime el tipo de dato de la variable, en este caso 'int'

# Flotante (float)
"""
Representa números decimales, es decir, números con parte fraccionaria.
"""
flotante = 3.14
print(flotante)
print(type(flotante)) # Imprime el tipo de dato de la variable, en este caso 'float'

# Cadena de caracteres (str)
"""
Representa una secuencia de caracteres. Puede contener letras, números, y otros caracteres.
"""
cadena = "¡Hola, Python!"
print(cadena)
print(type(cadena)) # Imprime el tipo de dato de la variable, en este caso 'str'

# Booleano (bool)
"""
Representa valores de verdad, es decir, True (verdadero) o False (falso).
"""
booleano = True
print(booleano)
print(type(booleano)) # Imprime el tipo de dato de la variable, en este caso 'bool'
booleano = False
print(booleano)
print(type(booleano)) # Imprime el tipo de dato de la variable, en este caso 'bool'

# Numero complejo (complex)
"""
Un número complejo consta de dos partes: la parte real y la parte imaginaria. 
Se expresan en la forma a + bj, donde a es la parte real, b es la parte imaginaria 
y j es la unidad imaginaria (que es la raíz cuadrada de -1).
"""
complejo = 1 + 2j
print(complejo)
print(type(complejo)) # Imprime el tipo de dato de la variable, en este caso 'complex'

# NoneType
"""
El tipo de dato None representa la ausencia de un valor o la falta de un objeto. 
Se utiliza comúnmente para indicar que una variable no tiene un valor asignado.
"""
nulo = None
print(nulo)
print(type(nulo)) # Imprime el tipo de dato de la variable, en este caso 'NoneType'

# Lista (list)
"""
Representa una secuencia mutable de elementos. 
Puedes modificar, añadir o eliminar elementos de una lista.
"""
lista = [1, 2, 3]
print(lista)
print(type(lista))

# Tupla (tuple)
"""
Similar a una lista, pero es inmutable, lo que significa que 
no puedes modificar su contenido después de crearla.
"""
tupla = (4, 5, 6)
print(tupla)
print(type(tupla)) # Imprime el tipo de dato de la variable, en este caso 'tuple'

# Conjunto (set)
"""
Representa una colección desordenada de elementos únicos. No permite elementos duplicados.
"""
conjunto = {7, 8, 9}
print(conjunto)
print(type(conjunto)) # Imprime el tipo de dato de la variable, en este caso 'set'

# Diccionario (dict)
"""
Representa una colección de pares clave-valor. Cada valor está asociado con una clave única.
"""
diccionario = {"a": 1, "b": 2, "c": 3}
print(diccionario)
print(type(diccionario)) # Imprime el tipo de dato de la variable, en este caso 'dict'

# Ejercicio: Imprime una cadena de caracteres (el mítico "Hola, Python!")
print("¡Hola, Python!") # Imprime la cadena de caracteres "¡Hola, Python!"
'''
Una pequeña anotación para aquel ineterasdo que haya llegado hasta aqui, yo esoy usando
 VSCode como editor de código y me he enamorado de el siguiente tema:
 en Configuración ve a "themes" y ponte uno que se llama Monokai, a mi me encanta jejejejej <3.
 '''
