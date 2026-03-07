#EJ 01 Factorial Recursivo

##recursion
def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"Factorial(0): {factorial(0)}")    # 1
print(f"Factorial(5): {factorial(5)}")    # 120
print(f"Factorial(10): {factorial(10)}")  # 3,628,800 

##for
def factorial_for(n):
    if n < 0:
        raise ValueError("n no puede ser negativo")

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

##While
def factorial_while(n):
    if n < 0:
        raise ValueError("n no puede ser negativo")

    resultado = 1
    i = 1
    while i <= n:
        resultado *= i
        i += 1
    return resultado

#EJ 02 Suma de Dígitos

##recursion
 def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# Pruebas
print(f"Suma dígitos(1234): {suma_digitos(1234)}") # 10
print(f"Suma dígitos(98765): {suma_digitos(98765)}") # 35

##for
def suma_digitos_for(n):
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma

##While
def suma_digitos_while(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma

#EJ 03 Búsqueda Binaria Recursiva

##resursion
def busqueda_binaria(arr, objetivo, izq, der):
    # Caso base 1: no encontrado
    if izq > der:
        return -1
    
    medio = (izq + der) // 2
    
    # Caso base 2: encontrado
    if arr[medio] == objetivo:
        return medio
    
    # Caso recursivo
    if objetivo < arr[medio]:
        return busqueda_binaria(arr, objetivo, izq, medio - 1)
    else:
        return busqueda_binaria(arr, objetivo, medio + 1, der)

# Prueba
lista = [2, 5, 8, 12, 16, 23, 38, 45, 72, 91]
print(f"Buscar 23: índice {busqueda_binaria(lista, 23, 0, len(lista)-1)}") # 5
##for
def busqueda_binaria_for(arr, objetivo):
    izq = 0
    der = len(arr) - 1

    for _ in range(len(arr)):
        if izq > der:
            return -1

        medio = (izq + der) // 2

        if arr[medio] == objetivo:
            return medio
        elif objetivo < arr[medio]:
            der = medio - 1
        else:
            izq = medio + 1

    return -1

##While
def busqueda_binaria_while(arr, objetivo):
    izq = 0
    der = len(arr) - 1

    while izq <= der:
        medio = (izq + der) // 2

        if arr[medio] == objetivo:
            return medio
        elif objetivo < arr[medio]:
            der = medio - 1
        else:
            izq = medio + 1

    return -1

#EJ 04 Palíndromo Recursivo

 ##recursion
def es_palindromo(texto):
    # Preprocesamiento (solo se hace en la primera llamada idealmente)
    # Aquí lo hacemos simple para cumplir el requisito
    texto = "".join(texto.lower().split())
    
    # Caso base
    if len(texto) <= 1:
        return True
    
    # Caso recursivo
    if texto[0] == texto[-1]:
        return es_palindromo(texto[1:-1])
    
    return False

# Pruebas
print(f"'anita': {es_palindromo('anita')}") # True
print(f"'python': {es_palindromo('python')}") # False

##for
def es_palindromo_for(texto):
    texto = texto.replace(" ", "").lower()

    for i in range(len(texto) // 2):
        if texto[i] != texto[-(i + 1)]:
            return False

    return True

##While
def es_palindromo_while(texto):
    texto = texto.replace(" ", "").lower()

    i = 0
    j = len(texto) - 1

    while i < j:
        if texto[i] != texto[j]:
            return False
        i += 1
        j -= 1

    return True

#EJ 05 Torres de Hanói

##recursion

def hanoi(n, origen, destino, auxiliar):
    # Caso base
    if n == 0:
        return
    
    # Mover n-1 discos de origen a auxiliar
    hanoi(n - 1, origen, auxiliar, destino)
    
    # Mover el disco más grande a destino
    print(f"Mover disco {n} de {origen} a {destino}")
    
    # Mover los n-1 discos de auxiliar a destino
    hanoi(n - 1, auxiliar, destino, origen)

# Prueba para n=3 (debe generar 7 movimientos)
print("--- Torres de Hanói (n=3) ---")
hanoi(3, "A", "C", "B")

#for
def hanoi_for(n, origen, destino, auxiliar):
    total = (2**n) - 1
    if n % 2 == 0:
        destino, auxiliar = auxiliar, destino

    for i in range(1, total + 1):
        if i % 3 == 1:
            print(f"Mover disco de {origen} a {destino}")
        elif i % 3 == 2:
            print(f"Mover disco de {origen} a {auxiliar}")
        elif i % 3 == 0:
            print(f"Mover disco de {auxiliar} a {destino}")

hanoi_for(3, "A", "C", "B")

#While
def hanoi_while(n, origen, destino, auxiliar):
    i = 1
    total = (2**n) - 1
    if n % 2 == 0:
        destino, auxiliar = auxiliar, destino

    while i <= total:
        if i % 3 == 1:
            print(f"Mover disco de {origen} a {destino}")
        elif i % 3 == 2:
            print(f"Mover disco de {origen} a {auxiliar}")
        elif i % 3 == 0:
            print(f"Mover disco de {auxiliar} a {destino}")
        i += 1
hanoi_while(3, "A", "C", "B")

##Multiplicación mediante Sumas
##recrusion
def multiplicar(a, b):
    # Manejo de a == 0
    if a == 0:
        return 0
    # Caso base
    if b == 0:
        return 0
    # Caso recursivo
    return a + multiplicar(a, b - 1)

# Pruebas
print(f"Multiplicar(4, 3): {multiplicar(4, 3)}") # 12
print(f"Multiplicar(6, 6): {multiplicar(6, 6)}") # 36

##for
def multiplicar_con_for(a, b):
    # Si b es 0, el rango será vacío y retornará 0 directamente
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado

# Pruebas
print(f"For: 4 * 3 = {multiplicar_con_for(4, 3)}")  # 12
print(f"For: 7 * 0 = {multiplicar_con_for(7, 0)}")  # 0

##while
def multiplicar_con_while(a, b):
    resultado = 0
    contador = b
    
    while contador > 0:
        resultado += a
        contador -= 1  # Decrementamos para no crear un bucle infinito
        
    return resultado

# Pruebas
print(f"While: 6 * 6 = {multiplicar_con_while(6, 6)}") # 36
print(f"While: 0 * 9 = {multiplicar_con_while(0, 9)}") # 0
