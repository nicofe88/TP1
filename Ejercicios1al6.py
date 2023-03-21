"""Escribir una función que calcule el máximo común divisor entre dos números"""

def calcular_mcd(a, b):
    if b == 0:
        return a
    else:
        return calcular_mcd(b, a % b)



""" Escribir una función que calcule el mínimo común múltiplo entre dos números """

def calcular_mcm(a, b):
    # Encontrar el número mayor
    mayor = max(a, b)
    # Iterar desde el número mayor hasta un múltiplo común
    for i in range(mayor, a*b+1, mayor):
        # Si el número actual es un múltiplo común, devolverlo
        if i % a == 0 and i % b == 0:
            return i
    # Si no se encuentra un múltiplo común, devolver a*b
    return a*b


""" Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia)."""

def contar_alabras(cadena):
    # Eliminar los caracteres especiales y convertir todo a minúsculas
    cadena = cadena.lower()
    caracteres_especiales = [',', '.', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '\"', '\'']
    for caracter in caracteres_especiales:
        cadena = cadena.replace(caracter, '')
    
    # Dividir la cadena en palabras y contar la frecuencia de cada una
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia


"""
Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
"""

def contar_palabras(cadena):
    # Eliminar los caracteres especiales y convertir todo a minúsculas
    cadena = cadena.lower()
    caracteres_especiales = [',', '.', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '\"', '\'']
    for caracter in caracteres_especiales:
        cadena = cadena.replace(caracter, '')
    
    # Dividir la cadena en palabras y contar la frecuencia de cada una
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia


def palabra_mas_repetida(diccionario):
    # Encontrar la palabra con la frecuencia más alta
    palabra_mas_repetida = max(diccionario, key=diccionario.get)
    frecuencia_mas_alta = diccionario[palabra_mas_repetida]
    
    return (palabra_mas_repetida, frecuencia_mas_alta)


"""
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva
"""

# Implementación iterativa
def get_int():
    while True:
        try:
            valor = int(input("Ingrese un número entero: "))
            return valor
        except ValueError:
            print("Error: debe ingresar un número entero.")


# Implementación recursiva
def get_int_recursivo():
    try:
        valor = int(input("Ingrese un número entero: "))
        return valor
    except ValueError:
        print("Error: debe ingresar un número entero.")
        return get_int_recursivo()


"""Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad"""


class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        if edad < 0:
            print("Error: la edad debe ser mayor o igual a cero.")
        else:
            self.edad = edad

    def set_dni(self, dni):
        if len(dni) != 8:
            print("Error: el DNI debe tener 8 dígitos.")
        else:
            self.dni = dni

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18
