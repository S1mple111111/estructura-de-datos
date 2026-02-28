#EJ 01 Factorial Recursivo

##if
def factorial_if(n):
    if n < 0:
        raise ValueError("n no puede ser negativo")
    if n == 0:
        return 1

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

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

##if
def suma_digitos_if(n):
    if n < 0:
        raise ValueError("Debe ser un entero positivo")

    suma = 0
    for d in str(n):
        suma += int(d)
    return suma

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

##if
def busqueda_binaria(arr, objetivo, izq, der):
    if izq > der:                 
        return -1

    medio = (izq + der) // 2

    if arr[medio] == objetivo:    
        return medio
    elif objetivo < arr[medio]:   
        return busqueda_binaria(arr, objetivo, izq, medio - 1)
    else:                         
        return busqueda_binaria(arr, objetivo, medio + 1, der)

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

 ##if
def es_palindromo(texto):
    texto = texto.replace(" ", "").lower()

    if len(texto) <= 1:
        return True

    if texto[0] != texto[-1]:
        return False

    return es_palindromo(texto[1:-1])

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

##if
def hanoi_recursivo(n, origen, destino, auxiliar):
    if n > 0:
        hanoi_recursivo(n - 1, origen, auxiliar, destino)
        print(f"Mover disco {n} de {origen} a {destino}")
        hanoi_recursivo(n - 1, auxiliar, destino, origen)

hanoi_recursivo(3, "A", "C", "B")

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