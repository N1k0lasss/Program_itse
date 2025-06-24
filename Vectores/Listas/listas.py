# Listas en python

# Crear una lista vacia
lista = []

# Crear una lista con un elemento
lista = [1]

# Crear una lista con varios elementos
lista = [1, 2, 3]

# Crear una lista con varios elementos y separados por comas
lista = [1, 2, 3]

# Crear una lista con varios elementos y separados por comas
lista = ['uno', 'dos', 'tres']

# Crear una lista con varios elementos y separados por comas
lista = ["uno", "dos", "tres"]

# Crear una lista con varios elementos y separados por comas
lista = tuple('uno', 'dos', 'tres')


#  Uso de listas

#  Ejemplo 1

lista = [1, 2, 3, 4, 5]

print(lista[0])  # Imprime el primer elemento de la lista
print(lista[1])  # Imprime el segundo elemento de la lista
print(lista[2])  # Imprime el tercer elemento de la lista
print(lista[3])  # Imprime el cuarto elemento de la lista
print(lista[4])  # Imprime el quinto elemento de la lista

#  Ejemplo 2

lista = [1, 2, 3, 4, 5]

print(lista[0:2])  # Imprime los dos primeros elementos de la lista
print(lista[2:4])  # Imprime los dos elementos de la lista desde el tercero
print(lista[4:])  # Imprime los elementos de la lista desde el quinto

#  Ejemplo 3

lista = [1, 2, 3, 4, 5]

print(lista[:2])  # Imprime los dos primeros elementos de la lista
print(lista[2:])  # Imprime los elementos de la lista desde el tercero

#  Ejemplo 4

lista = [1, 2, 3, 4, 5]

print(lista[:])  # Imprime toda la lista

#  Ejemplo 5

lista = [1, 2, 3, 4, 5]

print(lista[::-1])  # Imprime la lista invertida

#  Ejemplo 6

lista = [1, 2, 3, 4, 5]

# Imprime los elementos de la lista desde el segundo hasta el tercero con pasos de 2
print(lista[1:3:2])

#  Ejemplo 7

lista = [1, 2, 3, 4, 5]

for i in range(len(lista)):
    print(lista[i])
